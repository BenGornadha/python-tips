import pandas as pd

from cc_pandas.ep1.droppers.droppers import RowDropper, ColumnDropper

if __name__ == '__main__':
    df = pd.DataFrame({
        "First--Name": ["Alice", "Bob", "Charlie"],
        "Last Name": ["Smith", "Johnson", "Williams"],
        "Age in Years": [None, 30, 35],
        "Email Address": [None, "bob@example.com", "charlie@example.com"],
        "Phone Number": [None, "555-5678", "555-9876"]
    })

    row_dropper = RowDropper(maximum_missing_percentage_accepted=0.5)
    df_missing_row_cleaned = row_dropper.drop(df=df)

    column_dropper = ColumnDropper(maximum_missing_percentage_accepted=0.5)
    df_cleaned = column_dropper.drop(df=df_missing_row_cleaned)

    print(df_cleaned)