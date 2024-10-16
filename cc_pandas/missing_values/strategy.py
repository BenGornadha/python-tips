import pandas as pd

from typing import Protocol


class Strategy(Protocol):
    def apply(self, df: pd.DataFrame, column: str) -> pd.DataFrame:
        ...


class MeanStrategy:
    def apply(self, df: pd.DataFrame, column: str) -> pd.DataFrame:
        mean_value = df[column].mean()
        df[column] = df[column].fillna(mean_value)
        return df


class MedianStrategy:
    def apply(self, df: pd.DataFrame, column: str) -> pd.DataFrame:
        median_value = df[column].median()
        df[column] = df[column].fillna(median_value)
        return df
