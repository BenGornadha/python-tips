import pandas as pd
from typing import Union

from cc_pandas.missing_values.strategy import Strategy, MeanStrategy, MedianStrategy


class MissingValueReplacer:
    def __init__(self, column: str, replacement_value: Union[str, int, float]):
        self.column = column
        self.replacement_value = replacement_value

    def replace(self, df: pd.DataFrame) -> pd.DataFrame:
        df[self.column] = df[self.column].fillna(self.replacement_value)
        return df


class MissingValueFiller:
    def __init__(self, strategy: Strategy) -> None:
        self.strategy = strategy

    def apply(self, df: pd.DataFrame, column: str) -> pd.DataFrame:
        if not pd.api.types.is_numeric_dtype(df[column]):
            raise ValueError(f"The column {column} must contain numeric values to apply {self.strategy.__class__.__name__} strategy.")
        return self.strategy.apply(df=df, column=column)


