import pandas as pd

from cc_pandas.ep1.missing_values.strategy import Strategy




class MissingValueFiller:
    def __init__(self, strategy: Strategy) -> None:
        self.strategy = strategy

    def apply(self, df: pd.DataFrame, column: str) -> pd.DataFrame:
        if not pd.api.types.is_numeric_dtype(df[column]):
            raise ValueError(f"The column {column} must contain numeric values to apply {self.strategy.__class__.__name__} strategy.")
        return self.strategy.apply(df=df, column=column)


