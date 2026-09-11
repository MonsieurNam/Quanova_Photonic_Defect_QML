from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

from quanova_qml.data.splits import assert_split_safe
from quanova_qml.models.photonic import (
    PhotonicReservoir,
    merlin_collision_free_features,
    perceval_probabilities,
)


def verify_project(root: Path, with_perceval: bool = True) -> dict:
    split_files = sorted((root / "data" / "splits").glob("fold*_seed*_budget*.csv"))
    for path in split_files:
        assert_split_safe(pd.read_csv(path))
    reservoir = PhotonicReservoir()
    values = np.asarray([0.1, -0.2, 0.3, -0.4, 0.5])
    result = reservoir.probabilities(values)
    checks = {
        "split_files": len(split_files),
        "probability_sum": float(result.full_probabilities.sum()),
        "acceptance": result.acceptance,
        "conditional_sum": float(result.conditional_features.sum()),
        "outcomes_total": len(reservoir.outcomes),
        "outcomes_collision_free": len(reservoir.collision_free_indices),
    }
    if with_perceval:
        reference = perceval_probabilities(reservoir.circuit(values), reservoir.input_occupation)
        expected = np.asarray([reference.get(state, 0.0) for state in reservoir.outcomes])
        checks["perceval_max_abs_error"] = float(np.max(np.abs(expected - result.full_probabilities)))
        if checks["perceval_max_abs_error"] > 1e-9:
            raise AssertionError("Internal simulator does not match Perceval")
        merlin = merlin_collision_free_features(reservoir, values)
        checks["merlin_max_abs_error"] = float(
            np.max(np.abs(merlin - result.conditional_features))
        )
        if checks["merlin_max_abs_error"] > 1e-9:
            raise AssertionError("Internal collision-free features do not match MerLin")
    (root / "results" / "summaries").mkdir(parents=True, exist_ok=True)
    (root / "results" / "summaries" / "verification.json").write_text(
        json.dumps(checks, indent=2), encoding="utf-8"
    )
    return checks
