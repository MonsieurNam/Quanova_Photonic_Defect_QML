from __future__ import annotations

import json
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import joblib
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, balanced_accuracy_score, classification_report, f1_score
from sklearn.svm import SVC

from quanova_qml.features.preprocess import FullPreprocessor, PCA5Preprocessor
from quanova_qml.models.maps import make_map
from quanova_qml.utils import write_json

FAMILY_NAMES = {
    "B1": "Full CLIP + logistic regression",
    "B2": "Full CLIP + RBF-SVM",
    "B3": "PCA-5 + logistic regression",
    "B4": "PCA-5 + RBF-SVM",
    "B5": "PCA-5 + RFF-15 + logistic regression",
    "B6": "PCA-5 + ELM-15 + logistic regression",
    "Q1": "PCA-5 + photonic-15 + logistic regression",
}


@dataclass
class FittedPipeline:
    family: str
    preprocessor: Any
    feature_map: Any
    classifier: Any
    classes: list[str]

    def features(self, x: np.ndarray):
        transformed = self.preprocessor.transform(x)
        if self.feature_map is None:
            return transformed, None
        if self.family == "Q1":
            return self.feature_map.transform(transformed, return_acceptance=True)
        return self.feature_map.transform(transformed), None

    def predict(self, x: np.ndarray):
        features, acceptance = self.features(x)
        return self.classifier.predict(features), _scores(self.classifier, features), acceptance


def candidate_grid(family: str, model_cfg: dict) -> list[dict]:
    if family in {"B1", "B3"}:
        return [{"C": float(c)} for c in model_cfg["logistic_c"]]
    if family in {"B2", "B4"}:
        return [
            {"C": float(c), "scale": float(scale)}
            for c in model_cfg["rbf_c"]
            for scale in model_cfg["rbf_scales"]
        ]
    return [
        {"C": float(c), "scale": float(scale)}
        for c in model_cfg["matched_c"]
        for scale in model_cfg.get("feature_scales", [0.5, 1.0, 2.0])
    ]


def _classifier(family: str, candidate: dict):
    if family in {"B2", "B4"}:
        return SVC(
            C=candidate["C"],
            gamma=candidate["scale"] / 5.0,
            class_weight="balanced",
            decision_function_shape="ovr",
        )
    return LogisticRegression(
        C=candidate["C"], max_iter=5000, class_weight="balanced", random_state=42
    )


def _scores(model, x: np.ndarray) -> np.ndarray:
    if hasattr(model, "predict_proba"):
        return model.predict_proba(x)
    score = model.decision_function(x)
    return score[:, None] if score.ndim == 1 else score


def _metrics(y_true: np.ndarray, y_pred: np.ndarray, classes: list[str]) -> dict:
    return {
        "macro_f1": float(f1_score(y_true, y_pred, labels=classes, average="macro", zero_division=0)),
        "balanced_accuracy": float(balanced_accuracy_score(y_true, y_pred)),
        "accuracy": float(accuracy_score(y_true, y_pred)),
        "per_class": classification_report(
            y_true, y_pred, labels=classes, output_dict=True, zero_division=0
        ),
    }


def _fit_one(
    family: str,
    candidate: dict,
    map_seed: int | None,
    x_train: np.ndarray,
    y_train: np.ndarray,
    width: int,
) -> FittedPipeline:
    preprocessor = FullPreprocessor() if family in {"B1", "B2"} else PCA5Preprocessor()
    preprocessor.fit(x_train)
    train_reduced = preprocessor.transform(x_train)
    feature_map = None
    train_features = train_reduced
    if family in {"B5", "B6", "Q1"}:
        feature_map = make_map(family, width, candidate["scale"], int(map_seed))
        feature_map.fit(train_reduced)
        train_features = feature_map.transform(train_reduced)
    classifier = _classifier(family, candidate)
    classifier.fit(train_features, y_train)
    return FittedPipeline(family, preprocessor, feature_map, classifier, sorted(set(y_train)))


def evaluate_family(
    family: str,
    x_train: np.ndarray,
    y_train: np.ndarray,
    x_val: np.ndarray,
    y_val: np.ndarray,
    x_test: np.ndarray,
    y_test: np.ndarray,
    sample_ids: list[str],
    output_dir: Path,
    model_cfg: dict,
    map_seeds: list[int],
    width: int = 15,
    resume: bool = False,
) -> dict:
    complete_path = output_dir / "metrics.json"
    if resume and complete_path.exists():
        return json.loads(complete_path.read_text(encoding="utf-8"))
    output_dir.mkdir(parents=True, exist_ok=True)
    candidates = candidate_grid(family, model_cfg)
    seeds: list[int | None] = map_seeds if family in {"B5", "B6", "Q1"} else [None]
    rows, fitted = [], {}
    preprocessor = FullPreprocessor() if family in {"B1", "B2"} else PCA5Preprocessor()
    preprocessor.fit(x_train)
    train_reduced = preprocessor.transform(x_train)
    val_reduced = preprocessor.transform(x_val)
    map_cache: dict[tuple[int, float], tuple[Any, np.ndarray, np.ndarray]] = {}
    for config_order, candidate in enumerate(candidates):
        for map_seed in seeds:
            start = time.perf_counter()
            feature_map = None
            train_features, val_features = train_reduced, val_reduced
            acceptance = None
            if family in {"B5", "B6", "Q1"}:
                cache_key = (int(map_seed), float(candidate["scale"]))
                if cache_key not in map_cache:
                    feature_map = make_map(family, width, candidate["scale"], int(map_seed))
                    feature_map.fit(train_reduced)
                    train_features = feature_map.transform(train_reduced)
                    if family == "Q1":
                        val_features, acceptance = feature_map.transform(
                            val_reduced, return_acceptance=True
                        )
                    else:
                        val_features = feature_map.transform(val_reduced)
                    map_cache[cache_key] = (feature_map, train_features, val_features)
                else:
                    feature_map, train_features, val_features = map_cache[cache_key]
                    if family == "Q1":
                        _, acceptance = feature_map.transform(val_reduced, return_acceptance=True)
            classifier = _classifier(family, candidate)
            classifier.fit(train_features, y_train)
            pipeline = FittedPipeline(
                family, preprocessor, feature_map, classifier, sorted(set(y_train))
            )
            val_pred = classifier.predict(val_features)
            rows.append(
                {
                    "config_order": config_order,
                    "candidate": json.dumps(candidate, sort_keys=True),
                    "C": candidate["C"],
                    "scale": candidate.get("scale"),
                    "map_seed": map_seed,
                    "validation_macro_f1": f1_score(
                        y_val, val_pred, labels=pipeline.classes, average="macro", zero_division=0
                    ),
                    "validation_mean_acceptance": None
                    if acceptance is None
                    else float(np.mean(acceptance)),
                    "fit_validation_seconds": time.perf_counter() - start,
                }
            )
            fitted[(config_order, map_seed)] = pipeline
    candidate_frame = pd.DataFrame(rows)
    means = (
        candidate_frame.groupby(["config_order", "candidate", "C"], as_index=False, dropna=False)[
            "validation_macro_f1"
        ]
        .mean()
        .sort_values(
            ["validation_macro_f1", "C", "config_order"], ascending=[False, True, True]
        )
    )
    chosen_order = int(means.iloc[0]["config_order"])
    chosen_candidate = candidates[chosen_order]
    candidate_frame["selected_config"] = candidate_frame["config_order"] == chosen_order
    candidate_frame.to_csv(output_dir / "candidate_registry.csv", index=False)

    evaluations, predictions = [], []
    for map_seed in seeds:
        pipeline = fitted[(chosen_order, map_seed)]
        start = time.perf_counter()
        pred, scores, acceptance = pipeline.predict(x_test)
        metric = _metrics(y_test, pred, pipeline.classes)
        metric.update(
            {
                "map_seed": map_seed,
                "candidate": chosen_candidate,
                "test_inference_seconds": time.perf_counter() - start,
                "mean_acceptance": None if acceptance is None else float(np.mean(acceptance)),
            }
        )
        evaluations.append(metric)
        for idx, sample_id in enumerate(sample_ids):
            row = {
                "sample_id": sample_id,
                "true_label": y_test[idx],
                "prediction": pred[idx],
                "map_seed": map_seed,
                "failure": False,
                "acceptance": None if acceptance is None else acceptance[idx],
            }
            for class_idx, label in enumerate(pipeline.classifier.classes_):
                row[f"score_{label}"] = scores[idx, class_idx]
            predictions.append(row)
        joblib.dump(pipeline, output_dir / f"selected_seed{map_seed}.joblib")
    pd.DataFrame(predictions).to_csv(output_dir / "predictions.csv", index=False)
    metrics = {
        "family": family,
        "family_name": FAMILY_NAMES[family],
        "candidate_fits": len(rows),
        "test_evaluations": len(evaluations),
        "selected_candidate": chosen_candidate,
        "selection_rule": "mean validation macro-F1; lower C; locked config order",
        "evaluations": evaluations,
    }
    write_json(complete_path, metrics)
    return metrics


def evaluate_sampled_pipeline(
    pipeline: FittedPipeline,
    x_test: np.ndarray,
    y_test: np.ndarray,
    sample_ids: list[str],
    launched_shots: int,
    sampling_seed: int,
    output_dir: Path,
) -> dict:
    reduced = pipeline.preprocessor.transform(x_test)
    sampled, accepted, rejected, failures = pipeline.feature_map.sample(
        reduced, launched_shots, sampling_seed
    )
    prediction = pipeline.classifier.predict(sampled).astype(object)
    prediction[failures] = "__ABSTAIN__"
    scores = _scores(pipeline.classifier, sampled)
    metrics = _metrics(y_test, prediction, pipeline.classes)
    metrics.update(
        {
            "launched_shots": launched_shots,
            "sampling_seed": sampling_seed,
            "failures": int(failures.sum()),
            "mean_accepted": float(accepted.mean()),
            "mean_rejected": float(rejected.mean()),
            "acceptance_rate": float(accepted.sum() / (len(accepted) * launched_shots)),
        }
    )
    rows = []
    for idx, sample_id in enumerate(sample_ids):
        row = {
            "sample_id": sample_id,
            "true_label": y_test[idx],
            "prediction": prediction[idx],
            "failure": bool(failures[idx]),
            "launched_shots": launched_shots,
            "accepted": accepted[idx],
            "rejected": rejected[idx],
        }
        for class_idx, label in enumerate(pipeline.classifier.classes_):
            row[f"score_{label}"] = scores[idx, class_idx]
        rows.append(row)
    output_dir.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(output_dir / "predictions.csv", index=False)
    write_json(output_dir / "metrics.json", metrics)
    return metrics
