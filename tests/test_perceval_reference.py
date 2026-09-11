import numpy as np
import pytest

from quanova_qml.models.photonic import (
    PhotonicReservoir,
    merlin_collision_free_features,
    perceval_probabilities,
)


def test_internal_simulator_matches_perceval():
    pytest.importorskip("perceval")
    model = PhotonicReservoir(map_seed=303, scale=1.0)
    values = np.asarray([0.1, 0.3, -0.5, 0.7, -0.9])
    actual = model.probabilities(values).full_probabilities
    reference = perceval_probabilities(model.circuit(values), model.input_occupation)
    expected = np.asarray([reference.get(state, 0.0) for state in model.outcomes])
    assert np.allclose(actual, expected, atol=1e-9)
    merlin = merlin_collision_free_features(model, values)
    assert np.allclose(merlin, model.probabilities(values).conditional_features, atol=1e-9)
