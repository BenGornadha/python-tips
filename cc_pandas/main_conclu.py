import pandas as pd

if __name__ == '__main__':
    df = pd.DataFrame({
        "First-Name": ["Alice", "Bob", "Charlie"],
        "Last Name": ["Smith", "Johnson", "Williams"],
        "Age": [25, 30, 35],
        "Score": [85, None, 90],
        "Email Address": ["alice@example.com", "bob@example.com", "charlie@example.com"],
        "Phone Number": ["555-1234", "555-5678", "555-9876"]
    })

    new_columns = []
    for col in df.columns:
        col = col.strip()
        col = col.replace(' ', '_')
        col = col.replace('-', '_')
        col = col.lower()
        new_columns.append(col)
    df_snake = df.copy()
    for i in range(len(df.columns)):
        df_snake.rename(columns={df.columns[i]: new_columns[i]}, inplace=True)

    threshold_row = int(0.5 * len(df.columns))
    df_cleaned_rows = df.dropna(axis=0, thresh=threshold_row)

    threshold_col = int(0.5 * len(df))
    df_cleaned_columns = df.dropna(axis=1, thresh=threshold_col)

    mean_age = df["Age"].mean()
    df["Age"] = df["Age"].fillna(mean_age)

    mean_score = df["Score"].mean()
    df["Score"] = df["Score"].fillna(mean_score)

    median_score = df["Score"].median()
    df["Score"] = df["Score"].fillna(median_score)

