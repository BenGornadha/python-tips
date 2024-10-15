import pandas as pd


if __name__ == '__main__':
    df = pd.DataFrame({
        "First--Name": ["Alice", "Bob", "Charlie"],
        "Last Name": ["Smith", "Johnson", "Williams"],
        "Age in Years": [None, 30, 35],
        "Email Address": [None, "bob@example.com", "charlie@example.com"],
        "Phone Number": [None, "555-5678", "555-9876"]
    })

    threshold_row = int(0.5 * len(df.columns))
    df_cleaned_rows = df.dropna(axis=0, thresh=threshold_row)

    threshold_col = int(0.5 * len(df))
    df_cleaned_columns = df.dropna(axis=1, thresh=threshold_col)

    print("\nDataFrame après avoir supprimé les lignes avec plus de 50% de NaN :")
    print(df_cleaned_rows)