import pandas as pd
import numpy as np
from a import OutlierDetector

# Génération des données
if __name__ == '__main__':

    np.random.seed(42)  # Pour des résultats reproductibles
    data = {
        "A": np.random.normal(50, 10, 1000).tolist() + [500],  # Une valeur aberrante
        "B": np.random.normal(30, 5, 1000).tolist() + [300],   # Une valeur aberrante
        "C": np.random.choice(["X", "Y", "Z"], 1001)           # Colonne non numérique
    }
    df = pd.DataFrame(data)

    print(df.head())  # Affiche un aperçu des données
    print(df.shape)  # Affiche un aperçu des données
    detector = OutlierDetector(df)
    filtered_df = detector.filter_zscore_outliers(with_threshold=3.0)
    print(filtered_df.head())
    print(filtered_df.shape)