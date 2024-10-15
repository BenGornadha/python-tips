import pandas as pd

from cc_pandas.droppers.droppers import RowDropper, ColumnDropper

if __name__ == '__main__':
    df = pd.DataFrame({
        "First--Name": ["Alice", "Bob", "Charlie"],
        "Last Name": ["Smith", "Johnson", "Williams"],
        "Age in Years": [None, 30, 35],
        "Email Address": [None, "bob@example.com", "charlie@example.com"],
        "Phone Number": [None, "555-5678", "555-9876"]
    })

    fifty_percent_missing_row_dropper = RowDropper(minimum_missing_percentage_accepted=0.5)
    df_missing_row_cleaned = fifty_percent_missing_row_dropper.drop(df=df)

    fifty_percent_missing_column_dropper = ColumnDropper(minimum_missing_percentage_accepted=0.5)
    df_cleaned = fifty_percent_missing_column_dropper.drop(df=df_missing_row_cleaned)

    print(df_cleaned)