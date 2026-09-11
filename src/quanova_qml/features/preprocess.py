from __future__ import annotations

import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler, StandardScaler


class FullPreprocessor:
    def __init__(self):
        self.scaler = StandardScaler()

    def fit(self, x: np.ndarray) -> FullPreprocessor:
        self.scaler.fit(x)
        return self

    def transform(self, x: np.ndarray) -> np.ndarray:
        return self.scaler.transform(x)


class PCA5Preprocessor:
    def __init__(self):
        self.pca = PCA(n_components=5, random_state=42)
        self.scaler = MinMaxScaler(feature_range=(-np.pi, np.pi), clip=True)

    def fit(self, x: np.ndarray) -> PCA5Preprocessor:
        reduced = self.pca.fit_transform(x)
        self.scaler.fit(reduced)
        return self

    def transform(self, x: np.ndarray) -> np.ndarray:
        return self.scaler.transform(self.pca.transform(x))
