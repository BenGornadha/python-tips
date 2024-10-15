import pandas as pd
from typing import Union, Any

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


if __name__ == '__main__':

    df = pd.DataFrame({
        "Name": ["Alice", "Bob", "Charlie", None],
        "Age": [25, 30, None, 35],
        "Score": [85, None, 90, None]
    })

    mean_filler = MissingValueFiller(strategy=MeanStrategy())
    df_with_mean = mean_filler.apply(df=df, column='Age')

    median_filler = MissingValueFiller(strategy=MedianStrategy())
    df_with_median = median_filler.apply(df=df, column='Score')

    print(df_with_mean)
    print(df_with_median)