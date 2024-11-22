import pandas as pd

from cc_pandas.ep2.outliers.detector.detectors import BaseOutlierDetector


class OutlierMask:
    def __init__(self, dataframe: pd.DataFrame) -> None:
        self._df = dataframe.copy(deep=True)
        self._masks = pd.DataFrame(index=self._df.index)

    def generate_mask(self, column: str, outlier_detector: BaseOutlierDetector) -> None:
        self._masks[column] = outlier_detector.apply()

    def combine_masks(self, max_outliers: int) -> pd.Series:
        num_outliers_per_row = (~self._masks).sum(axis=1)
        return num_outliers_per_row <= max_outliers
