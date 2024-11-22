import pandas as pd


def clean_cols(df):
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
    return df_snake


if __name__ == '__main__':
    df = pd.DataFrame({
        "First-Name": ["Alice", "Bob", "Charlie"],
        "Last Name": ["Smith", "Johnson", "Williams"],
        "Age in Years": [25, 30, 35],
        "Email Address": ["alice@example.com", "bob@example.com", "charlie@example.com"],
        "Phone Number": ["555-1234", "555-5678", "555-9876"]
    })

    df = clean_cols(df)
    print(df)
