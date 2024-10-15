import pandas as pd

from cc_pandas.missing_values.missing_value import MissingValueReplacer

from typing import Protocol

class Strategy(Protocol):
    def apply(self, df: pd.DataFrame, column: str) -> pd.DataFrame:
        ...

class MeanStrategy:
    def apply(self, df: pd.DataFrame, column: str) -> pd.DataFrame:
        mean_value = df[column].mean()
        return MissingValueReplacer(column=column, replacement_value=mean_value).replace(df)


class MedianStrategy:
    def apply(self, df: pd.DataFrame, column: str) -> pd.DataFrame:
        median_value = df[column].median()
        return MissingValueReplacer(column=column, replacement_value=median_value).replace(df)
