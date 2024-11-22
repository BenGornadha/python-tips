import pandas as pd

from cc_pandas.ep2.outliers.gaussian_checker.gaussian_checkers import GaussianChecker, GaussianCheckerShapiro


class OutlierZScore:
    def __init__(self, a_series: pd.Series, threshold=3.0):
        self._a_series = a_series.copy(deep=True)
        self._threshold = threshold

    def apply(self) -> pd.Series:
        mean = self._a_series.mean()
        std_dev = self._a_series.std()
        return (self._a_series - mean).abs() <= self._threshold * std_dev


class OutlierDetector:
    def __init__(self, a_dataframe: pd.DataFrame, gaussian_checker : GaussianChecker = GaussianCheckerShapiro()) -> None:
        self._df = a_dataframe.copy(deep=True)
        self._gaussian_checker = gaussian_checker

    def filter_zscore_outliers(self, with_threshold=3.0) -> pd.DataFrame:
        for column in self._df.select_dtypes(include='number').columns:
            current_series = self._df[column]
            if self._gaussian_checker.is_gaussian(a_series=current_series):
                self._df = self._df[OutlierZScore(a_series=current_series, threshold=with_threshold).apply()]
        return self._df

