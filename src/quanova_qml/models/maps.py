from __future__ import annotations

import numpy as np
from sklearn.kernel_approximation import RBFSampler

from .photonic import PhotonicReservoir


class RFFMap:
    def __init__(self, width: int, scale: float, seed: int):
        self.map = RBFSampler(gamma=scale, n_components=width, random_state=seed)

    def fit(self, x: np.ndarray) -> RFFMap:
        self.map.fit(x)
        return self

    def transform(self, x: np.ndarray) -> np.ndarray:
        return self.map.transform(x)


class ELMMap:
    def __init__(self, input_width: int, width: int, scale: float, seed: int):
        rng = np.random.default_rng(seed)
        self.weights = rng.normal(size=(input_width, width)) * scale / np.sqrt(input_width)
        self.bias = rng.uniform(-np.pi, np.pi, size=width)

    def fit(self, x: np.ndarray) -> ELMMap:
        return self

    def transform(self, x: np.ndarray) -> np.ndarray:
        return np.tanh(x @ self.weights + self.bias)


def make_map(family: str, width: int, scale: float, seed: int):
    if family == "B5":
        return RFFMap(width, scale, seed)
    if family == "B6":
        return ELMMap(5, width, scale, seed)
    if family == "Q1":
        return PhotonicReservoir(map_seed=seed, scale=scale)
    raise ValueError(f"No feature map for {family}")
