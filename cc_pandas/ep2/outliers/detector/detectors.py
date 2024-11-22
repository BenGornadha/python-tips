from abc import ABC, abstractmethod

import pandas as pd


class BaseOutlierDetector(ABC):

    def __init__(self):
        self._current_series = pd.Series()

    @abstractmethod
    def apply(self):
        raise NotImplementedError

    def with_series(self, current_series: pd.Series) -> None:
        self._current_series = current_series

    def flush(self):
        self._current_series = pd.Series()


class OutlierDetectorZScore(BaseOutlierDetector):
    def __init__(self, threshold: float = 3.0):
        super().__init__()
        self.threshold = threshold

    def apply(self) -> pd.Series:
        mean = self._current_series.mean()
        std_dev = self._current_series.std()
        return (self._current_series - mean).abs() <= self.threshold * std_dev


class OutlierDetectorIQR(BaseOutlierDetector):
    def __init__(self, multiplier: float = 1.5):
        super().__init__()
        self.multiplier = multiplier

    def apply(self) -> pd.Series:
        q1 = self._current_series.quantile(0.25)
        q3 = self._current_series.quantile(0.75)
        iqr = q3 - q1

        lower_bound = q1 - self.multiplier * iqr
        upper_bound = q3 + self.multiplier * iqr

        return (self._current_series >= lower_bound) & (self._current_series <= upper_bound)
