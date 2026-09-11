import numpy as np
import pandas as pd
import pytest

from quanova_qml.data.splits import assert_split_safe
from quanova_qml.features.preprocess import PCA5Preprocessor
from quanova_qml.runner import count_work


def test_split_rejects_duplicate_group_leakage():
    unsafe = pd.DataFrame(
        {
            "sample_id": ["a", "b"],
            "duplicate_group": ["same", "same"],
            "split": ["train", "test"],
        }
    )
    with pytest.raises(AssertionError):
        assert_split_safe(unsafe)


def test_test_data_cannot_change_train_fitted_preprocessor():
    rng = np.random.default_rng(4)
    train = rng.normal(size=(50, 20))
    test = rng.normal(size=(10, 20))
    preprocessing = PCA5Preprocessor().fit(train)
    before_mean = preprocessing.pca.mean_.copy()
    original = preprocessing.transform(test)
    changed = preprocessing.transform(test + 10_000)
    assert np.array_equal(before_mean, preprocessing.pca.mean_)
    assert not np.allclose(original, changed)


def test_locked_work_counts():
    common = {
        "families": ["B1", "B2", "B3", "B4", "B5", "B6", "Q1"],
        "subset_seeds": [11, 22, 33],
        "budgets": [12, 24, 48],
    }
    pilot = count_work({**common, "profile": "pilot", "folds": [0]})
    full = count_work({**common, "profile": "full", "folds": [0, 1, 2, 3, 4]})
    minimum = count_work(
        {**common, "profile": "pilot_min", "folds": [0], "subset_seeds": [11], "budgets": [24]}
    )
    assert (pilot["candidate_fits"], pilot["test_evaluations"]) == (1404, 117)
    assert (full["candidate_fits"], full["test_evaluations"]) == (7020, 585)
    assert (minimum["candidate_fits"], minimum["test_evaluations"]) == (156, 13)
