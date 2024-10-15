import pandas as pd
from typing import  Optional


class RowDropper:
    def __init__(self, minimum_missing_percentage_accepted: Optional[float] = None):
        self.minimum_missing_threshold_accepted = minimum_missing_percentage_accepted

    def _require_non_empty_dataframe(self, df: pd.DataFrame) -> None:
        if df.empty:
            raise ValueError("The DataFrame is empty. Nothing to drop.")

    def _compute_minimum_non_missing_values_accepted(self, df: pd.DataFrame) -> int:
        nb_columns = df.shape[1]
        if self.minimum_missing_threshold_accepted is None:
            return nb_columns
        return int((1 - self.minimum_missing_threshold_accepted) * nb_columns)

    def drop_missing_rows(self, df: pd.DataFrame) -> pd.DataFrame:
        self._require_non_empty_dataframe(df=df)
        minimum_non_missing_values_accepted = self._compute_minimum_non_missing_values_accepted(df=df)
        return df.dropna(thresh=minimum_non_missing_values_accepted)


class ColumnDropper:
    def __init__(self, minimum_missing_percentage_accepted: Optional[float] = None):
        self.minimum_missing_percentage_accepted = minimum_missing_percentage_accepted

    def _require_non_empty_dataframe(self, df: pd.DataFrame) -> None:
        if df.empty:
            raise ValueError("The DataFrame is empty. Nothing to drop.")

    def _compute_minimum_non_missing_values_accepted(self, df: pd.DataFrame) -> int:
        nb_rows = df.shape[0]
        if self.minimum_missing_percentage_accepted is None:
            return nb_rows
        return int((1 - self.minimum_missing_percentage_accepted) * nb_rows)

    def drop_missing_columns(self, df: pd.DataFrame) -> pd.DataFrame:
        self._require_non_empty_dataframe(df=df)
        minimum_non_missing_values_accepted = self._compute_minimum_non_missing_values_accepted(df=df)
        return df.dropna(axis=1, thresh=minimum_non_missing_values_accepted)

if __name__ == '__main__':
    df = pd.DataFrame({
        "First--Name": ["Alice", "Bob", "Charlie"],
        "Last Name": ["Smith", "Johnson", "Williams"],
        "Age in Years": [None, 30, 35],
        "Email Address": [None, "bob@example.com", "charlie@example.com"],
        "Phone Number": [None, "555-5678", "555-9876"]
    })

    # Supprimer les lignes qui contiennent des valeurs manquantes
    forty_percent_missing_row_dropper = RowDropper(minimum_missing_percentage_accepted=0.5)
    df_cleaned = forty_percent_missing_row_dropper.drop_missing_rows(df=df)

    print(df_cleaned)