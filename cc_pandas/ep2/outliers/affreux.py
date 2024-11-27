import numpy as np
import pandas as pd
from scipy.stats import shapiro


if __name__ == '__main__':

    np.random.seed(42)
    data = {
        "A": np.random.normal(50, 10, 50).tolist() + [500],
        "B": np.random.normal(30, 5, 50).tolist() + [300],
        "C": np.random.choice(["X", "Y", "Z"], 51)
    }
    df = pd.DataFrame(data)

    for col in df.select_dtypes(include='number').columns:
        col_data = df[col]
        stat, pvalue = shapiro(col_data[(col_data - col_data.mean()).abs() <= 3 * col_data.std()])
        if pvalue > 0.05:
            mean_val = col_data.mean()
            std_dev_val = col_data.std()
            df[col] = col_data.where((col_data - mean_val).abs() <= 3 * std_dev_val, mean_val)

    rows_outliers = (~df.select_dtypes(include='number').apply(
        lambda x: ((x - x.mean()).abs() <= 3 * x.std()), axis=0)).sum(axis=1)
    df = df[rows_outliers <= 2]

    print(df)



