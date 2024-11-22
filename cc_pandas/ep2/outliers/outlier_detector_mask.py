import pandas as pd

from cc_pandas.ep2.outliers.detector.detectors import OutlierDetectorZScore
from cc_pandas.ep2.outliers.gaussian_checker.gaussian_checkers import GaussianChecker, GaussianCheckerShapiro
from cc_pandas.ep2.outliers.mask.mask import OutlierMask


class OutlierDetector2:
    def __init__(self, a_dataframe: pd.DataFrame, gaussian_checker: GaussianChecker = GaussianCheckerShapiro()) -> None:
        self._df = a_dataframe.copy(deep=True)
        self._gaussian_checker = gaussian_checker
        self._outlier_mask = OutlierMask(dataframe=self._df)

    def filter_zscore_outliers(self, with_threshold=3.0, max_outliers_per_row=1) -> pd.DataFrame:
        for column in self._df.select_dtypes(include='number').columns:
            self._detect_outlier_for(column=column, with_threshold=with_threshold)

        global_mask = self._outlier_mask.combine_masks(max_outliers=max_outliers_per_row)

        return self._df[global_mask]

    def _detect_outlier_for(self, column: str, with_threshold: float) -> None:
        current_series = self._df[column]
        if self._gaussian_checker.is_gaussian(a_series=current_series):
            outlier_detector = OutlierDetectorZScore(a_series=current_series, threshold=with_threshold)
            self._outlier_mask.generate_mask(column=column, outlier_detector=outlier_detector)
