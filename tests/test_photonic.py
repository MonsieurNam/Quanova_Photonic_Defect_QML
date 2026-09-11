import numpy as np

from quanova_qml.models.photonic import PhotonicReservoir, fock_outcomes


def test_locked_outcomes_and_probabilities():
    model = PhotonicReservoir()
    result = model.probabilities(np.zeros(5))
    assert len(fock_outcomes(6, 2)) == 21
    assert result.conditional_features.shape == (15,)
    assert np.isclose(result.full_probabilities.sum(), 1.0, atol=1e-10)
    assert np.isclose(result.conditional_features.sum(), 1.0, atol=1e-10)
    assert 0 <= result.acceptance <= 1


def test_input_changes_distribution():
    model = PhotonicReservoir(map_seed=101)
    first = model.probabilities(np.zeros(5)).full_probabilities
    second = model.probabilities(np.asarray([0.2, -0.4, 0.6, -0.8, 1.0])).full_probabilities
    assert not np.allclose(first, second)


def test_sampling_accounts_for_every_launched_shot():
    model = PhotonicReservoir(map_seed=202)
    _, accepted, rejected, failures = model.sample(np.zeros((3, 5)), 500, 77)
    assert np.all(accepted + rejected == 500)
    assert failures.dtype == bool
