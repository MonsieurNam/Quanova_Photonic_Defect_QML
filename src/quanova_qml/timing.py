from __future__ import annotations

import time
from pathlib import Path

import numpy as np
import pandas as pd

from quanova_qml.features.clip import load_embeddings
from quanova_qml.features.preprocess import PCA5Preprocessor
from quanova_qml.models.photonic import PhotonicReservoir
from quanova_qml.utils import write_json


def time_quantum_map(cfg: dict, root: Path) -> dict:
    embeddings, _ = load_embeddings(root / cfg["project"]["embeddings"])
    split_path = root / cfg["project"]["splits_dir"] / "fold0_seed11_budget24.csv"
    split = pd.read_csv(split_path)
    train = split.loc[split["split"] == "train"]
    validation = split.loc[split["split"] == "validation"]
    allowed = pd.concat([train, validation], ignore_index=True)
    n = min(int(cfg["runtime"]["timing_inputs"]), len(allowed))
    selected = allowed.sample(n=n, random_state=cfg["project"]["seed"])
    x_train = np.stack([embeddings[item] for item in train["sample_id"]])
    x_selected = np.stack([embeddings[item] for item in selected["sample_id"]])
    preprocess = PCA5Preprocessor().fit(x_train)
    reduced = preprocess.transform(x_selected)
    model = PhotonicReservoir(map_seed=101, scale=1.0)
    start = time.perf_counter()
    model.transform(reduced)
    seconds = time.perf_counter() - start
    per_input = seconds / n

    # Nine unique (map seed, scale) maps per cell. Counts use metadata only; timing inputs never use test.
    projected_inputs = 0
    for fold in [0]:
        for subset_seed in cfg["data"]["subset_seeds"]:
            for budget in sorted(int(key) for key in cfg["data"]["budgets"]):
                path = root / cfg["project"]["splits_dir"] / f"fold{fold}_seed{subset_seed}_budget{budget}.csv"
                counts = pd.read_csv(path, usecols=["split"])["split"].value_counts()
                projected_inputs += 9 * int(counts.sum())
    projected_seconds = per_input * projected_inputs
    result = {
        "timing_source": "64 or fewer train/validation inputs only",
        "timed_inputs": n,
        "seconds": seconds,
        "seconds_per_circuit_input": per_input,
        "projected_r1_unique_map_inputs": projected_inputs,
        "projected_r1_quantum_feature_hours": projected_seconds / 3600,
        "threshold_hours": cfg["runtime"]["max_pilot_hours"],
        "recommended_profile": "pilot_min"
        if projected_seconds / 3600 > cfg["runtime"]["max_pilot_hours"]
        else "pilot",
        "caveat": "Projection covers quantum feature generation, not CLIP extraction or classifier fitting.",
    }
    write_json(root / "results" / "summaries" / "timing_gate.json", result)
    return result
