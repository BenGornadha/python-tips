import pandas as pd
from typing import Optional

from cc_pandas.droppers.port import Dropper


class RowDropper(Dropper):
    def __init__(self, minimum_missing_percentage_accepted: Optional[float] = None):
        self.minimum_missing_percentage_accepted = minimum_missing_percentage_accepted

    def _compute_minimum_non_missing_values_accepted(self, nb_columns: int) -> int:
        if self.minimum_missing_percentage_accepted is None:
            return nb_columns
        return int((1 - self.minimum_missing_percentage_accepted) * nb_columns) + 1 # + 1 is for odd nb cols

    def drop(self, df: pd.DataFrame) -> pd.DataFrame:
        self._require_non_empty_dataframe(df=df)
        minimum_non_missing_values_accepted = self._compute_minimum_non_missing_values_accepted(nb_columns=df.shape[1])
        return df.dropna(axis=0,thresh=minimum_non_missing_values_accepted)


class ColumnDropper(Dropper):
    def __init__(self, minimum_missing_percentage_accepted: Optional[float] = None):
        self.minimum_missing_percentage_accepted = minimum_missing_percentage_accepted

    def _compute_minimum_non_missing_values_accepted(self, nb_rows: int) -> int:
        if self.minimum_missing_percentage_accepted is None:
            return nb_rows
        return int((1 - self.minimum_missing_percentage_accepted) * nb_rows)

    def drop(self, df: pd.DataFrame) -> pd.DataFrame:
        self._require_non_empty_dataframe(df=df)
        minimum_non_missing_values_accepted = self._compute_minimum_non_missing_values_accepted(nb_rows=df.shape[0])
        return df.dropna(axis=1, thresh=minimum_non_missing_values_accepted)
