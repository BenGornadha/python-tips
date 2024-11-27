import pandas as pd
import numpy as np

from cc_pandas.ep2.outliers.detector.detectors import OutlierDetectorIQR, OutlierDetectorZScore
from cc_pandas.ep2.outliers.gaussian_checker.gaussian_checkers import GaussianCheckerKSTest, GaussianCheckerShapiro
from cc_pandas.ep2.outliers.outlier_detector_mask_2 import OutlierRemover


if __name__ == '__main__':

    np.random.seed(42)
    data = {
        "A": np.random.normal(50, 10, 50).tolist() + [500],
        "B": np.random.normal(30, 5, 50).tolist() + [300],
        "C": np.random.choice(["X", "Y", "Z"], 51)
    }
    df = pd.DataFrame(data)

    outlier_remover = OutlierRemover(a_dataframe=df,
                                     outlier_detector=OutlierDetectorZScore(),
                                     gaussian_checker=GaussianCheckerShapiro())
    filtered_df = outlier_remover.filter_outliers(max_outliers_per_row=3)

    print(filtered_df.tail())
