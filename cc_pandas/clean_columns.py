import pandas as pd
import re
from typing import List



class ColumnCleaner:

    def __init__(self, column_name: str):
        self.column_name = column_name

    def convert_to_snake_case(self) -> str:
        return re.sub(r'[-\s]+', '_', self.column_name.strip().lower())

    def convert_to_camel_case(self) -> str:
        words = re.split(r'\s+|_|-', self.column_name.strip())
        return words[0].lower() + ''.join(word.capitalize() for word in words[1:])


class ColumnsCleaner:
    def __init__(self, columns: List[str]):
        self.columns = columns

    def all_to_snake_case(self) -> List[str]:
        return [ColumnCleaner(column_name=column_name).convert_to_snake_case() for column_name in self.columns]

    def all_to_camel_case(self) -> List[str]:
        return [ColumnCleaner(column_name=column_name).convert_to_camel_case() for column_name in self.columns]

    @staticmethod
    def snake_case_columns_for(df: pd.DataFrame) -> pd.DataFrame:
        cleaner = ColumnsCleaner(columns=df.columns.tolist())
        snake_case_columns = cleaner.all_to_snake_case()
        return df.rename(columns=dict(zip(df.columns, snake_case_columns)))

    @staticmethod
    def camel_case_columns_for(df: pd.DataFrame) -> pd.DataFrame:
        cleaner = ColumnsCleaner(columns=df.columns.tolist())
        camel_case_columns = cleaner.all_to_camel_case()
        return df.rename(columns=dict(zip(df.columns, camel_case_columns)))


if __name__ == '__main__':
    df = pd.DataFrame({
        "First-Name": ["Alice", "Bob", "Charlie"],
        "Last Name": ["Smith", "Johnson", "Williams"],
        "Age in Years": [25, 30, 35],
        "Email Address": ["alice@example.com", "bob@example.com", "charlie@example.com"],
        "Phone Number": ["555-1234", "555-5678", "555-9876"]
    })

    df_camel_case = ColumnsCleaner.camel_case_columns_for(df)
    print(df_camel_case)

    print("---"*100)

    df_snake_case = ColumnsCleaner.snake_case_columns_for(df)
    print(df_snake_case)



