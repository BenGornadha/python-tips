import pandas as pd

from cc_pandas.ep2.outliers.detector.detectors import OutlierDetectorZScore, BaseOutlierDetector
from cc_pandas.ep2.outliers.gaussian_checker.gaussian_checkers import GaussianChecker, GaussianCheckerShapiro
from cc_pandas.ep2.outliers.mask.mask import OutlierMask


class OutlierRemover:
    def __init__(self, a_dataframe: pd.DataFrame,
                 gaussian_checker: GaussianChecker = GaussianCheckerShapiro(),
                 outlier_detector: BaseOutlierDetector = OutlierDetectorZScore()) -> None:

        self._df = a_dataframe.copy(deep=True)
        self._gaussian_checker = gaussian_checker
        self._outlier_detector = outlier_detector
        self._outlier_mask = OutlierMask(dataframe=self._df)

    def filter_outliers(self, max_outliers_per_row: int = 1):
        for column in self._df.select_dtypes(include='number').columns:
            current_series = self._df[column]
            if self._gaussian_checker.is_gaussian(a_series=current_series):
                self._outlier_detector.with_series(current_series)
                self._outlier_mask.generate_mask(column=column, outlier_detector=self._outlier_detector)

        global_mask = self._outlier_mask.combine_masks(max_outliers=max_outliers_per_row)

        return self._df[global_mask]
