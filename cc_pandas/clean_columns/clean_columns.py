import re
import pandas as pd

from cc_pandas.clean_columns.port import ColumnFormatter


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
