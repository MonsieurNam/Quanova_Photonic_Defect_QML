from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedGroupKFold

from quanova_qml.utils import sha256_file, write_json


def _ordered_class_pool(frame: pd.DataFrame, label: str, seed: int) -> pd.DataFrame:
    subset = frame.loc[frame["label"] == label].copy()
    rng = np.random.default_rng(seed)
    groups = subset["duplicate_group"].drop_duplicates().to_numpy()
    rng.shuffle(groups)
    rank = {group: idx for idx, group in enumerate(groups)}
    subset["_rank"] = subset["duplicate_group"].map(rank)
    return subset.sort_values(["_rank", "sample_id"]).drop(columns="_rank")


def create_splits(
    manifest_csv: Path,
    splits_dir: Path,
    budgets: dict,
    subset_seeds: list[int],
    n_folds: int = 5,
    outer_seed: int = 42,
) -> dict:
    manifest = pd.read_csv(manifest_csv)
    clean = manifest.loc[(manifest["valid"] == True) & (manifest["quarantine"] == False)].copy()
    splitter = StratifiedGroupKFold(n_splits=n_folds, shuffle=True, random_state=outer_seed)
    splits_dir.mkdir(parents=True, exist_ok=True)
    index_rows: list[dict] = []
    for fold, (pool_idx, test_idx) in enumerate(
        splitter.split(clean, clean["label"], groups=clean["duplicate_group"])
    ):
        pool, test = clean.iloc[pool_idx], clean.iloc[test_idx]
        test_groups = set(test["duplicate_group"])
        inner = StratifiedGroupKFold(n_splits=5, shuffle=True, random_state=outer_seed + fold)
        full_train_idx, full_val_idx = next(
            inner.split(pool, pool["label"], groups=pool["duplicate_group"])
        )
        full_train, full_val = pool.iloc[full_train_idx], pool.iloc[full_val_idx]
        full_path = splits_dir / f"fold{fold}_seed42_budgetfull.csv"
        pd.concat(
            [
                full_train.assign(split="train"),
                full_val.assign(split="validation"),
                test.assign(split="test"),
            ],
            ignore_index=True,
        )[["sample_id", "path", "label", "duplicate_group", "sha256", "split"]].to_csv(
            full_path, index=False
        )
        index_rows.append(
            {
                "fold": fold,
                "subset_seed": 42,
                "budget": "full",
                "train": len(full_train),
                "validation": len(full_val),
                "test": len(test),
                "path": str(full_path),
                "sha256": sha256_file(full_path),
            }
        )
        for subset_seed in subset_seeds:
            per_class = {
                label: _ordered_class_pool(pool, label, subset_seed + 1009 * fold)
                for label in sorted(clean["label"].unique())
            }
            max_train = max(int(spec["train"]) for spec in budgets.values())
            max_val = max(int(spec["validation"]) for spec in budgets.values())
            for budget_key, spec in sorted(budgets.items(), key=lambda pair: int(pair[0])):
                train_rows, val_rows = [], []
                for label, ordered in per_class.items():
                    train_n, val_n = int(spec["train"]), int(spec["validation"])
                    if len(ordered) < max_train + max_val:
                        raise ValueError(f"Class {label} has only {len(ordered)} outer-pool images")
                    train_rows.append(ordered.iloc[:train_n])
                    val_rows.append(ordered.iloc[max_train : max_train + val_n])
                train = pd.concat(train_rows)
                val = pd.concat(val_rows)
                if set(train["duplicate_group"]) & set(val["duplicate_group"]):
                    raise AssertionError("duplicate group overlaps train and validation")
                if (set(train["duplicate_group"]) | set(val["duplicate_group"])) & test_groups:
                    raise AssertionError("duplicate group overlaps test")
                out = pd.concat(
                    [
                        train.assign(split="train"),
                        val.assign(split="validation"),
                        test.assign(split="test"),
                    ],
                    ignore_index=True,
                )[["sample_id", "path", "label", "duplicate_group", "sha256", "split"]]
                budget = int(budget_key)
                path = splits_dir / f"fold{fold}_seed{subset_seed}_budget{budget}.csv"
                out.to_csv(path, index=False)
                index_rows.append(
                    {
                        "fold": fold,
                        "subset_seed": subset_seed,
                        "budget": budget,
                        "train": len(train),
                        "validation": len(val),
                        "test": len(test),
                        "path": str(path),
                        "sha256": sha256_file(path),
                    }
                )
    index = pd.DataFrame(index_rows)
    index.to_csv(splits_dir / "index.csv", index=False)
    summary = {"n_split_files": len(index), "outer_folds": n_folds, "seed": outer_seed}
    write_json(splits_dir / "summary.json", summary)
    return summary


def assert_split_safe(frame: pd.DataFrame) -> None:
    by_group = frame.groupby("duplicate_group")["split"].nunique()
    if (by_group > 1).any():
        raise AssertionError("At least one duplicate group crosses split boundaries")
    by_id = frame.groupby("sample_id")["split"].nunique()
    if (by_id > 1).any():
        raise AssertionError("At least one sample ID crosses split boundaries")
