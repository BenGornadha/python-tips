import pandas as pd

from cc_pandas.clean_columns.clean_columns import ColumnsCleaner

if __name__ == '__main__':
    df = pd.DataFrame({
        "First--Name": ["Alice", "Bob", "Charlie"],
        "Last Name": ["Smith", "Johnson", "Williams"],
        "Age in Years": [25, 30, 35],
        "Email Address": ["alice@example.com", "bob@example.com", "charlie@example.com"],
        "Phone Number": ["555-1234", "555-5678", "555-9876"]
    })

    df_camel_case = ColumnsCleaner.all_to_snake_case(df=df)
    print(df_camel_case)

    print("---" * 100)

    df_snake_case = ColumnsCleaner.all_to_camel_case(df=df)
    print(df_snake_case)