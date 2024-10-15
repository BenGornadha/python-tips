from abc import ABC, abstractmethod

import pandas as pd
import re


class ColumnFormatter(ABC):

    @abstractmethod
    def convert(self, column_name: str) -> str:
        ...


class SnakeCaseFormatter(ColumnFormatter):
    def convert(self, column_name: str) -> str:
        return re.sub(r'[-\s]+', '_', column_name.strip().lower())


class CamelCaseFormatter(ColumnFormatter):
    def convert(self, column_name: str) -> str:
        words = re.split(r'\s+|_|-', column_name.strip())
        return words[0].lower() + ''.join(word.capitalize() for word in words[1:])


class ColumnsCleaner:

    @staticmethod
    def all_to_snake_case(df: pd.DataFrame) -> pd.DataFrame:
        snake_case_formatter = SnakeCaseFormatter()
        columns_snake_cased = [snake_case_formatter.convert(column_name=column_name) for column_name in df.columns]
        return df.rename(columns=dict(zip(df.columns, columns_snake_cased)))

    @staticmethod
    def all_to_camel_case(df: pd.DataFrame) -> pd.DataFrame:
        camel_case_formatter = CamelCaseFormatter()
        columns_camel_cased = [camel_case_formatter.convert(column_name=column_name) for column_name in df.columns]
        return df.rename(columns=dict(zip(df.columns, columns_camel_cased)))


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
