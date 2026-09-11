from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.metrics import confusion_matrix


def _save_figure(fig: plt.Figure, figure_dir: Path, stem: str, source: pd.DataFrame) -> None:
    source.to_csv(figure_dir / f"{stem}.csv", index=False)
    fig.tight_layout()
    for suffix in ["png", "svg", "pdf"]:
        fig.savefig(figure_dir / f"{stem}.{suffix}", dpi=220, bbox_inches="tight")
    plt.close(fig)


def _collect(root: Path) -> pd.DataFrame:
    rows = []
    for metrics_path in sorted((root / "runs").glob("*/metrics.json")):
        metrics = json.loads(metrics_path.read_text(encoding="utf-8"))
        config_path = metrics_path.parent / "config.json"
        config = json.loads(config_path.read_text(encoding="utf-8")) if config_path.exists() else {}
        for evaluation in metrics.get("evaluations", [metrics] if "macro_f1" in metrics else []):
            rows.append(
                {
                    "run_id": metrics_path.parent.name,
                    "profile": config.get("profile", "shots"),
                    "family": metrics.get("family", "Q1-sampled"),
                    "fold": config.get("fold", 0),
                    "subset_seed": config.get("subset_seed", 11),
                    "budget": str(config.get("budget", 24)),
                    "map_seed": evaluation.get("map_seed", metrics.get("map_seed")),
                    "sampling_seed": evaluation.get("sampling_seed"),
                    "launched_shots": evaluation.get("launched_shots"),
                    "macro_f1": evaluation["macro_f1"],
                    "balanced_accuracy": evaluation["balanced_accuracy"],
                    "accuracy": evaluation["accuracy"],
                    "acceptance": evaluation.get(
                        "mean_acceptance", evaluation.get("acceptance_rate")
                    ),
                    "failures": evaluation.get("failures", 0),
                    "test_inference_seconds": evaluation.get("test_inference_seconds"),
                }
            )
    if not rows:
        raise FileNotFoundError("No completed metrics under runs/")
    return pd.DataFrame(rows)


def _main_tables(table: pd.DataFrame, table_dir: Path) -> tuple[pd.DataFrame, pd.DataFrame]:
    raw = table.loc[table["profile"].eq("pilot")].copy()
    raw["budget"] = raw["budget"].astype(int)
    # A map seed is a repeated view of one subset. Average maps before subset summaries.
    units = (
        raw.groupby(["family", "budget", "subset_seed"], as_index=False)
        .agg(
            macro_f1=("macro_f1", "mean"),
            balanced_accuracy=("balanced_accuracy", "mean"),
            accuracy=("accuracy", "mean"),
            acceptance=("acceptance", "mean"),
            map_evaluations=("macro_f1", "size"),
        )
    )
    summary = (
        units.groupby(["family", "budget"], as_index=False)
        .agg(
            macro_f1_mean=("macro_f1", "mean"),
            macro_f1_std=("macro_f1", "std"),
            balanced_accuracy_mean=("balanced_accuracy", "mean"),
            accuracy_mean=("accuracy", "mean"),
            subset_count=("subset_seed", "size"),
        )
    )
    raw.to_csv(table_dir / "main_results_raw_evaluations.csv", index=False)
    units.to_csv(table_dir / "main_results_by_subset.csv", index=False)
    summary.to_csv(table_dir / "main_results.csv", index=False)
    return raw, summary


def _comparison_tables(raw: pd.DataFrame, table_dir: Path) -> tuple[pd.DataFrame, pd.DataFrame]:
    compression = (
        raw.loc[raw["family"].isin(["B1", "B2", "B3", "B4"])]
        .pivot_table(index=["budget", "subset_seed"], columns="family", values="macro_f1")
        .reset_index()
    )
    compression["B1_minus_B3"] = compression["B1"] - compression["B3"]
    compression["B2_minus_B4"] = compression["B2"] - compression["B4"]
    compression.to_csv(table_dir / "compression.csv", index=False)

    stochastic = raw.loc[raw["family"].isin(["B5", "B6", "Q1"])].pivot_table(
        index=["budget", "subset_seed", "map_seed"], columns="family", values="macro_f1"
    ).reset_index()
    stochastic["Q1_minus_RFF"] = stochastic["Q1"] - stochastic["B5"]
    stochastic["Q1_minus_ELM"] = stochastic["Q1"] - stochastic["B6"]
    b4 = raw.loc[raw["family"].eq("B4"), ["budget", "subset_seed", "macro_f1"]].rename(
        columns={"macro_f1": "B4"}
    )
    paired = stochastic.merge(b4, on=["budget", "subset_seed"], how="left")
    paired["Q1_minus_RBF"] = paired["Q1"] - paired["B4"]
    paired.to_csv(table_dir / "paired_differences.csv", index=False)
    return compression, paired


def _dataset_table(root: Path, table_dir: Path) -> None:
    path = root / "data" / "manifests" / "neu_cls.summary.json"
    if not path.exists():
        return
    summary = json.loads(path.read_text(encoding="utf-8"))
    rows = [
        {"metric": "images_total", "value": summary["images_total"]},
        {"metric": "valid", "value": summary["valid"]},
        {"metric": "quarantined", "value": summary["quarantined"]},
        {"metric": "exact_duplicate_groups", "value": summary["exact_duplicate_groups"]},
        {"metric": "conflicting_duplicate_groups", "value": summary["conflicting_duplicate_groups"]},
    ] + [
        {"metric": f"class_{label}", "value": count}
        for label, count in summary["class_counts"].items()
    ]
    pd.DataFrame(rows).to_csv(table_dir / "dataset_audit.csv", index=False)


def _runtime_table(root: Path, table: pd.DataFrame, table_dir: Path) -> pd.DataFrame:
    rows: list[dict] = []
    embedding_path = root / "cache" / "clip_vit_b32_openai.npz"
    if embedding_path.exists():
        archive = np.load(embedding_path, allow_pickle=False)
        metadata = json.loads(str(archive["metadata"]))
        rows.append({"stage": "CLIP embedding", "family": "all", "seconds": metadata["seconds"]})
    timing_path = root / "results" / "summaries" / "timing_gate.json"
    if timing_path.exists():
        timing = json.loads(timing_path.read_text(encoding="utf-8"))
        rows.append({"stage": "quantum timing sample", "family": "Q1", "seconds": timing["seconds"]})
    for run_dir in sorted((root / "runs").glob("pilot_*")):
        candidate_path = run_dir / "candidate_registry.csv"
        config_path = run_dir / "config.json"
        if candidate_path.exists() and config_path.exists():
            config = json.loads(config_path.read_text(encoding="utf-8"))
            rows.append(
                {
                    "stage": "candidate fit + validation",
                    "family": config["family"],
                    "seconds": pd.read_csv(candidate_path)["fit_validation_seconds"].sum(),
                }
            )
    inference = table.loc[table["profile"].eq("pilot")].groupby("family", as_index=False)[
        "test_inference_seconds"
    ].sum()
    rows += [
        {"stage": "test inference", "family": row.family, "seconds": row.test_inference_seconds}
        for row in inference.itertuples()
    ]
    runtime = pd.DataFrame(rows)
    runtime.to_csv(table_dir / "compute_cost.csv", index=False)
    return runtime


def _confusions(root: Path, figure_dir: Path) -> None:
    configs = []
    for path in (root / "runs").glob("pilot_*/config.json"):
        cfg = json.loads(path.read_text(encoding="utf-8"))
        if cfg["subset_seed"] == 11 and str(cfg["budget"]) == "24" and cfg["family"] in {"B1", "Q1"}:
            configs.append((cfg["family"], path.parent / "predictions.csv"))
    if len(configs) != 2:
        return
    frames = []
    labels = ["Cr", "In", "Pa", "PS", "RS", "Sc"]
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.2))
    for axis, (family, path) in zip(axes, sorted(configs)):
        prediction = pd.read_csv(path)
        matrix = confusion_matrix(
            prediction["true_label"], prediction["prediction"], labels=labels, normalize="true"
        )
        sns.heatmap(matrix, annot=True, fmt=".2f", cmap="Blues", vmin=0, vmax=1, ax=axis)
        axis.set(title=f"{family} — fold 0, subset 11, budget 24", xlabel="Predicted", ylabel="True")
        axis.set_xticklabels(labels)
        axis.set_yticklabels(labels, rotation=0)
        for i, true_label in enumerate(labels):
            for j, pred_label in enumerate(labels):
                frames.append({"family": family, "true_label": true_label, "prediction": pred_label, "rate": matrix[i, j]})
    _save_figure(fig, figure_dir, "confusion_b1_q1", pd.DataFrame(frames))


def summarize_runs(root: Path) -> dict:
    table = _collect(root)
    table_dir, figure_dir = root / "results" / "tables", root / "results" / "figures"
    table_dir.mkdir(parents=True, exist_ok=True)
    figure_dir.mkdir(parents=True, exist_ok=True)
    table.to_csv(table_dir / "all_evaluations.csv", index=False)
    raw, main = _main_tables(table, table_dir)
    _, paired = _comparison_tables(raw, table_dir)
    _dataset_table(root, table_dir)
    runtime = _runtime_table(root, table, table_dir)

    full_label = table.loc[table["profile"].eq("full_label")].copy()
    full_label.to_csv(table_dir / "full_label_results.csv", index=False)
    shots = table.loc[table["profile"].eq("shots")].copy()
    shots_summary = (
        shots.groupby("launched_shots", as_index=False)
        .agg(
            macro_f1_mean=("macro_f1", "mean"),
            macro_f1_std=("macro_f1", "std"),
            acceptance_mean=("acceptance", "mean"),
            failures=("failures", "sum"),
            evaluations=("macro_f1", "size"),
        )
    )
    shots.to_csv(table_dir / "finite_shot_raw.csv", index=False)
    shots_summary.to_csv(table_dir / "finite_shot.csv", index=False)

    sns.set_theme(style="whitegrid", context="talk")
    fig, ax = plt.subplots(figsize=(9, 5))
    sns.lineplot(data=main, x="budget", y="macro_f1_mean", hue="family", marker="o", ax=ax)
    ax.set(xlabel="Total labeled examples per class (train + validation)", ylabel="Macro-F1", ylim=(0, 1.02))
    _save_figure(fig, figure_dir, "learning_curve", main)

    delta_long = paired.melt(
        id_vars=["budget", "subset_seed", "map_seed"],
        value_vars=["Q1_minus_RFF", "Q1_minus_ELM", "Q1_minus_RBF"],
        var_name="comparison",
        value_name="macro_f1_difference",
    )
    fig, ax = plt.subplots(figsize=(9, 5))
    sns.pointplot(data=delta_long, x="budget", y="macro_f1_difference", hue="comparison", dodge=0.25, errorbar="sd", ax=ax)
    ax.axhline(0, color="black", linewidth=1)
    ax.set(xlabel="Labels per class", ylabel="Q1 minus baseline macro-F1")
    _save_figure(fig, figure_dir, "paired_quantum_differences", delta_long)

    compression_long = raw.loc[raw["family"].isin(["B1", "B2", "B3", "B4"])].copy()
    fig, ax = plt.subplots(figsize=(9, 5))
    sns.lineplot(data=compression_long, x="budget", y="macro_f1", hue="family", marker="o", errorbar="sd", ax=ax)
    ax.set(xlabel="Labels per class", ylabel="Macro-F1", ylim=(0, 1.02))
    _save_figure(fig, figure_dir, "compression_performance", compression_long)

    fig, left = plt.subplots(figsize=(8, 4.8))
    right = left.twinx()
    shot_positions = np.arange(len(shots_summary))
    left.errorbar(
        shot_positions,
        shots_summary["macro_f1_mean"],
        yerr=shots_summary["macro_f1_std"],
        marker="o",
        color="#16697A",
    )
    right.plot(
        shot_positions,
        shots_summary["acceptance_mean"],
        marker="s",
        color="#E76F51",
    )
    left.set(
        xticks=shot_positions,
        xticklabels=[f"{int(value):,}" for value in shots_summary["launched_shots"]],
        xlabel="Launched shots per image",
        ylabel="Macro-F1",
        ylim=(0, 1.02),
    )
    right.set(ylabel="Acceptance rate", ylim=(0, 1.02))
    _save_figure(fig, figure_dir, "finite_shot_sensitivity", shots_summary)

    runtime_plot = runtime.groupby(["stage", "family"], as_index=False)["seconds"].sum()
    fig, ax = plt.subplots(figsize=(9, 5))
    sns.barplot(data=runtime_plot, x="seconds", y="family", hue="stage", ax=ax)
    ax.set(xlabel="Measured wall-clock seconds", ylabel="Family")
    _save_figure(fig, figure_dir, "runtime_breakdown", runtime_plot)
    _confusions(root, figure_dir)

    summary = {
        "evaluations": len(table),
        "r1_evaluations": int((table["profile"] == "pilot").sum()),
        "r2_evaluations": int((table["profile"] == "full_label").sum()),
        "r3_evaluations": int((table["profile"] == "shots").sum()),
        "families": sorted(table["family"].unique()),
        "tables": len(list(table_dir.glob("*.csv"))),
        "figures": len(list(figure_dir.glob("*.png"))),
    }
    (root / "results" / "summaries" / "summary.json").write_text(
        json.dumps(summary, indent=2), encoding="utf-8"
    )
    return summary
