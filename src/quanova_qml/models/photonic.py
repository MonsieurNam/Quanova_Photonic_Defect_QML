from __future__ import annotations

import hashlib
import json
import math
from dataclasses import dataclass

import numpy as np


def fock_outcomes(modes: int, photons: int) -> list[tuple[int, ...]]:
    if photons != 2:
        raise NotImplementedError("The locked pilot implements exactly two photons")
    outcomes = []
    for left in range(modes):
        for right in range(left, modes):
            state = [0] * modes
            state[left] += 1
            state[right] += 1
            outcomes.append(tuple(state))
    return outcomes


def haar_unitary(modes: int, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    z = rng.normal(size=(modes, modes)) + 1j * rng.normal(size=(modes, modes))
    q, r = np.linalg.qr(z)
    phases = np.diag(r)
    phases = phases / np.where(np.abs(phases) == 0, 1, np.abs(phases))
    return q * phases.conj()


def _expanded_indices(occupation: tuple[int, ...]) -> list[int]:
    return [mode for mode, count in enumerate(occupation) for _ in range(count)]


def _permanent_2(matrix: np.ndarray) -> complex:
    return matrix[0, 0] * matrix[1, 1] + matrix[0, 1] * matrix[1, 0]


def transition_probability(
    unitary: np.ndarray, input_state: tuple[int, ...], output_state: tuple[int, ...]
) -> float:
    rows = _expanded_indices(output_state)
    columns = _expanded_indices(input_state)
    submatrix = unitary[np.ix_(rows, columns)]
    numerator = abs(_permanent_2(submatrix)) ** 2
    denominator = math.prod(math.factorial(v) for v in input_state) * math.prod(
        math.factorial(v) for v in output_state
    )
    return float(numerator / denominator)


@dataclass
class PhotonicResult:
    full_probabilities: np.ndarray
    conditional_features: np.ndarray
    acceptance: float


class PhotonicReservoir:
    """Six-mode/two-photon U -> phase(x) -> U reservoir locked for the pilot."""

    def __init__(
        self,
        modes: int = 6,
        input_occupation: tuple[int, ...] = (1, 0, 1, 0, 0, 0),
        map_seed: int = 101,
        scale: float = 1.0,
    ):
        self.modes = modes
        self.input_occupation = tuple(input_occupation)
        self.map_seed = map_seed
        self.scale = scale
        self.unitary = haar_unitary(modes, map_seed)
        self.outcomes = fock_outcomes(modes, sum(self.input_occupation))
        self.collision_free_indices = [
            idx for idx, state in enumerate(self.outcomes) if max(state) <= 1
        ]
        if len(self.outcomes) != 21 or len(self.collision_free_indices) != 15:
            raise AssertionError("Locked circuit must have 21 total and 15 collision-free outcomes")

    def fit(self, x: np.ndarray) -> PhotonicReservoir:
        """Sklearn-like no-op: the random circuit is fixed entirely by map_seed."""
        return self

    @property
    def circuit_hash(self) -> str:
        payload = {
            "modes": self.modes,
            "input": self.input_occupation,
            "map_seed": self.map_seed,
            "scale": self.scale,
            "unitary_real": self.unitary.real.round(15).tolist(),
            "unitary_imag": self.unitary.imag.round(15).tolist(),
        }
        return hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()

    def circuit(self, values: np.ndarray) -> np.ndarray:
        values = np.asarray(values, dtype=float)
        if values.shape != (self.modes - 1,):
            raise ValueError(f"Expected {self.modes - 1} phase values, got {values.shape}")
        phases = np.zeros(self.modes)
        phases[: self.modes - 1] = np.remainder(self.scale * values + np.pi, 2 * np.pi) - np.pi
        return self.unitary @ np.diag(np.exp(1j * phases)) @ self.unitary

    def probabilities(self, values: np.ndarray) -> PhotonicResult:
        circuit = self.circuit(values)
        full = np.asarray(
            [transition_probability(circuit, self.input_occupation, state) for state in self.outcomes]
        )
        full = np.clip(full, 0.0, None)
        total = float(full.sum())
        if not np.isclose(total, 1.0, atol=1e-9):
            full /= total
        accepted = full[self.collision_free_indices]
        acceptance = float(accepted.sum())
        conditional = accepted / acceptance if acceptance > 0 else np.zeros_like(accepted)
        return PhotonicResult(full, conditional, acceptance)

    def transform(self, x: np.ndarray, return_acceptance: bool = False):
        results = [self.probabilities(row) for row in np.asarray(x)]
        features = np.stack([item.conditional_features for item in results])
        acceptance = np.asarray([item.acceptance for item in results])
        return (features, acceptance) if return_acceptance else features

    def sample(self, x: np.ndarray, launched_shots: int, sampling_seed: int):
        rng = np.random.default_rng(sampling_seed)
        features, accepted_counts, rejected_counts, failures = [], [], [], []
        for row in np.asarray(x):
            result = self.probabilities(row)
            counts = rng.multinomial(launched_shots, result.full_probabilities)
            accepted = counts[self.collision_free_indices]
            accepted_count = int(accepted.sum())
            features.append(accepted / accepted_count if accepted_count else np.zeros(15))
            accepted_counts.append(accepted_count)
            rejected_counts.append(int(launched_shots - accepted_count))
            failures.append(accepted_count == 0)
        return (
            np.asarray(features),
            np.asarray(accepted_counts),
            np.asarray(rejected_counts),
            np.asarray(failures),
        )


def perceval_probabilities(unitary: np.ndarray, input_state: tuple[int, ...]) -> dict[tuple[int, ...], float]:
    """Optional reference used by smoke tests; requires perceval-quandela."""
    import perceval as pcvl

    circuit = pcvl.Circuit(unitary.shape[0])
    circuit.add(0, pcvl.Unitary(pcvl.Matrix(unitary)))
    backend = pcvl.BackendFactory().get_backend("SLOS")
    backend.set_circuit(circuit)
    backend.set_input_state(pcvl.BasicState(input_state))
    distribution = backend.prob_distribution()
    return {tuple(state): float(probability) for state, probability in distribution.items()}


def merlin_collision_free_features(model: PhotonicReservoir, values: np.ndarray) -> np.ndarray:
    """Run the same locked circuit through MerLin 0.4's unbunched probability layer."""
    import perceval as pcvl
    import torch
    from merlin import MeasurementStrategy, QuantumLayer

    matrix = pcvl.Matrix(model.unitary)
    encoder = pcvl.Circuit(model.modes)
    for idx in range(model.modes - 1):
        encoder.add(idx, pcvl.PS(pcvl.P(f"px{idx + 1}")))
    circuit = pcvl.Unitary(matrix) // encoder // pcvl.Unitary(matrix.copy())
    layer = QuantumLayer(
        input_size=model.modes - 1,
        circuit=circuit,
        input_state=list(model.input_occupation),
        trainable_parameters=[],
        input_parameters=["px"],
        measurement_strategy=MeasurementStrategy.probs(),
        dtype=torch.float64,
    )
    encoded = np.remainder(model.scale * np.asarray(values) + np.pi, 2 * np.pi) - np.pi
    with torch.inference_mode():
        return layer(torch.as_tensor(encoded[None, :], dtype=torch.float64)).numpy()[0]
