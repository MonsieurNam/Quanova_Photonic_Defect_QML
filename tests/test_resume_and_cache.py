import json

import numpy as np

from quanova_qml.features.clip import load_embeddings
from quanova_qml.models.benchmark import evaluate_family


def test_embedding_cache_round_trip(tmp_path):
    path = tmp_path / "embeddings.npz"
    ids = np.asarray(["a", "b"])
    vectors = np.arange(8, dtype=np.float32).reshape(2, 4)
    np.savez_compressed(path, sample_ids=ids, embeddings=vectors, metadata=np.asarray(json.dumps({"x": 1})))
    cache, metadata = load_embeddings(path)
    assert metadata == {"x": 1}
    assert np.array_equal(cache["b"], vectors[1])


def test_resume_does_not_duplicate_candidate_fits(tmp_path):
    rng = np.random.default_rng(8)
    x_train = rng.normal(size=(30, 8))
    y_train = np.asarray(["a", "b", "c"] * 10)
    x_val = rng.normal(size=(12, 8))
    y_val = np.asarray(["a", "b", "c"] * 4)
    x_test = rng.normal(size=(12, 8))
    y_test = np.asarray(["a", "b", "c"] * 4)
    cfg = {"logistic_c": [0.01, 0.1, 1.0, 10.0]}
    first = evaluate_family(
        "B1", x_train, y_train, x_val, y_val, x_test, y_test,
        [str(i) for i in range(12)], tmp_path, cfg, [101, 202, 303]
    )
    second = evaluate_family(
        "B1", x_train, y_train, x_val, y_val, x_test, y_test,
        [str(i) for i in range(12)], tmp_path, cfg, [101, 202, 303], resume=True
    )
    assert first == second
    assert len(list(tmp_path.glob("candidate_registry.csv"))) == 1
