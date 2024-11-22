import pandas as pd
import numpy as np

from cc_pandas.ep2.outliers.detector.detectors import OutlierDetectorIQR
from cc_pandas.ep2.outliers.gaussian_checker.gaussian_checkers import GaussianCheckerKSTest
from cc_pandas.ep2.outliers.outlier_detector_mask import OutlierDetector2
from cc_pandas.ep2.outliers.outlier_detector_mask_2 import OutlierDetector3
from outlier_detector import OutlierDetector

# Génération des données
if __name__ == '__main__':
    np.random.seed(42)  # Pour des résultats reproductibles
    data = {
        "A": np.random.normal(50, 10, 50).tolist() + [500],  # Une valeur aberrante
        "B": np.random.normal(30, 5, 50).tolist() + [300],  # Une valeur aberrante
        "C": np.random.choice(["X", "Y", "Z"], 51)  # Colonne non numérique
    }
    df = pd.DataFrame(data)

    print(df.tail())  # Affiche un aperçu des données
    print(df.shape)  # Affiche un aperçu des données

    detector = OutlierDetector3(a_dataframe=df,
                                outlier_detector=OutlierDetectorIQR(),
                                gaussian_checker=GaussianCheckerKSTest())
    filtered_df = detector.filter_outliers(max_outliers_per_row=1)
    print(filtered_df.tail())
    print(filtered_df.shape)
