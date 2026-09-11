from __future__ import annotations

import itertools
import json
from pathlib import Path

import joblib
import numpy as np
import pandas as pd

from quanova_qml.config import stable_hash
from quanova_qml.data.splits import assert_split_safe
from quanova_qml.features.clip import load_embeddings
from quanova_qml.models.benchmark import evaluate_family, evaluate_sampled_pipeline
from quanova_qml.utils import git_revision, sha256_file, write_json

DIRECT = {"B1", "B2", "B3", "B4"}
STOCHASTIC = {"B5", "B6", "Q1"}


def count_work(cfg: dict) -> dict:
    families = cfg["families"]
    cells = len(cfg["folds"]) * len(cfg["subset_seeds"]) * len(cfg["budgets"])
    fits_per_cell = 12 * len(DIRECT & set(families)) + 36 * len(STOCHASTIC & set(families))
    evals_per_cell = len(DIRECT & set(families)) + 3 * len(STOCHASTIC & set(families))
    return {
        "profile": cfg["profile"],
        "cells": cells,
        "candidate_fits": cells * fits_per_cell,
        "test_evaluations": cells * evals_per_cell,
    }


def _arrays(split: pd.DataFrame, embeddings: dict[str, np.ndarray]):
    missing = sorted(set(split["sample_id"]) - set(embeddings))
    if missing:
        raise KeyError(f"Missing {len(missing)} embeddings; first={missing[0]}")
    values = np.stack([embeddings[sample_id] for sample_id in split["sample_id"]])
    return values, split["label"].to_numpy(), split["sample_id"].tolist()


def run_benchmark(cfg: dict, root: Path, resume: bool = False) -> dict:
    embeddings, encoder_metadata = load_embeddings(root / cfg["project"]["embeddings"])
    model_cfg = dict(cfg["models"])
    model_cfg["feature_scales"] = cfg["quantum"]["feature_scales"]
    registry = []
    for fold, subset_seed, budget in itertools.product(
        cfg["folds"], cfg["subset_seeds"], cfg["budgets"]
    ):
        split_path = root / cfg["project"]["splits_dir"] / (
            f"fold{fold}_seed{subset_seed}_budget{budget}.csv"
        )
        split = pd.read_csv(split_path)
        assert_split_safe(split)
        train = split.loc[split["split"] == "train"]
        val = split.loc[split["split"] == "validation"]
        test = split.loc[split["split"] == "test"]
        x_train, y_train, _ = _arrays(train, embeddings)
        x_val, y_val, _ = _arrays(val, embeddings)
        x_test, y_test, test_ids = _arrays(test, embeddings)
        for family in cfg["families"]:
            identity = {
                "profile": cfg["profile"],
                "fold": fold,
                "subset_seed": subset_seed,
                "budget": budget,
                "family": family,
            }
            run_id = f"{cfg['profile']}_{stable_hash(identity, 12)}"
            output_dir = root / cfg["project"]["runs_dir"] / run_id
            run_config = {
                **identity,
                "run_id": run_id,
                "dataset_hash": sha256_file(split_path),
                "encoder": encoder_metadata,
                "code_version": git_revision(root),
                "train_ids": train["sample_id"].tolist(),
                "validation_ids": val["sample_id"].tolist(),
                "test_ids": test_ids,
            }
            write_json(output_dir / "config.json", run_config)
            metrics = evaluate_family(
                family,
                x_train,
                y_train,
                x_val,
                y_val,
                x_test,
                y_test,
                test_ids,
                output_dir,
                model_cfg,
                cfg["quantum"]["map_seeds"],
                cfg["models"]["feature_width"],
                resume,
            )
            registry.append({**identity, "run_id": run_id, **{k: metrics[k] for k in ["candidate_fits", "test_evaluations"]}})
    registry_frame = pd.DataFrame(registry)
    registry_frame.to_csv(root / "runs" / f"registry_{cfg['profile']}.csv", index=False)
    return {
        "runs": len(registry),
        "candidate_fits": int(registry_frame["candidate_fits"].sum()),
        "test_evaluations": int(registry_frame["test_evaluations"].sum()),
    }


def run_shots(cfg: dict, root: Path, resume: bool = False) -> dict:
    embeddings, _ = load_embeddings(root / cfg["project"]["embeddings"])
    split_path = root / cfg["project"]["splits_dir"] / "fold0_seed11_budget24.csv"
    split = pd.read_csv(split_path)
    test = split.loc[split["split"] == "test"]
    x_test, y_test, test_ids = _arrays(test, embeddings)
    identity = {
        "profile": "pilot",
        "fold": 0,
        "subset_seed": 11,
        "budget": 24,
        "family": "Q1",
    }
    ideal_dir = root / "runs" / f"pilot_{stable_hash(identity, 12)}"
    if not (ideal_dir / "metrics.json").exists():
        raise FileNotFoundError(
            "R3 requires the completed ideal R1 Q1 run; run configs/pilot.yaml first"
        )
    metrics = []
    for map_seed in cfg["quantum"]["map_seeds"]:
        pipeline = joblib.load(ideal_dir / f"selected_seed{map_seed}.joblib")
        for launched, sampling_seed in itertools.product(
            cfg["shots"]["launched"], cfg["shots"]["sampling_seeds"]
        ):
            shot_id = f"shots_q{map_seed}_n{launched}_s{sampling_seed}"
            output_dir = root / "runs" / shot_id
            if resume and (output_dir / "metrics.json").exists():
                metrics.append(json.loads((output_dir / "metrics.json").read_text(encoding="utf-8")))
                continue
            metric = evaluate_sampled_pipeline(
                pipeline, x_test, y_test, test_ids, launched, sampling_seed, output_dir
            )
            metric["map_seed"] = map_seed
            write_json(output_dir / "metrics.json", metric)
            metrics.append(metric)
    pd.DataFrame(metrics).to_csv(root / "runs" / "registry_shots.csv", index=False)
    return {"test_evaluations": len(metrics)}
