


import pandas as pd

if __name__ == '__main__':
    df = pd.DataFrame({
        "Name": ["Alice", "Bob", "Charlie", None],
        "Age": [25, 30, None, 35],
        "Score": [85, None, 90, None],
    })

    mean_age = df["Age"].mean()
    df["Age"] = df["Age"].fillna(mean_age)

    mean_score = df["Score"].mean()
    df["Score"] = df["Score"].fillna(mean_score)

    median_score = df["Score"].median()
    df["Score"] = df["Score"].fillna(median_score)

    print(df)
