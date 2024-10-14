import pandas as pd
from typing import Union, Optional


class MissingValueReplacer:
    def __init__(self, column: str, replacement_value: Union[str, int, float]):
        self.column = column
        self.replacement_value = replacement_value

    def replace(self, df: pd.DataFrame) -> pd.DataFrame:
        df[self.column] = df[self.column].fillna(self.replacement_value)
        return df


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


class MissingValueHandler:
    def __init__(self, strategy: str):
        self.strategy = strategy

    def apply(self, df: pd.DataFrame, column: str) -> pd.DataFrame:
        if self.strategy == 'mean':
            mean_value = df[column].mean()
            return MissingValueReplacer(column, mean_value).replace(df)
        elif self.strategy == 'median':
            median_value = df[column].median()
            return MissingValueReplacer(column, median_value).replace(df)
        else:
            raise ValueError("Unknown strategy. Supported strategies: 'mean', 'median'")


if __name__ == '__main__':
    # Exemple d'utilisation
    df = pd.DataFrame({
        "Name": ["Alice", "Bob", "Charlie", None],
        "Age": [25, 30, None, 35],
        "Score": [85, None, 90, None]
    })

    # Remplacer les valeurs manquantes de la colonne 'Age' par la moyenne
    mean_replacer = MissingValueHandler(strategy='mean')
    df_with_mean = mean_replacer.apply(df=df, column='Age')

    # Remplacer les valeurs manquantes de la colonne 'Score' par une valeur par défaut (ex. : 50)
    replacer = MissingValueReplacer(column="Score", replacement_value=50)
    df_with_default_score = replacer.replace(df=df_with_mean)

    # Supprimer les lignes qui contiennent des valeurs manquantes
    forty_percent_missing_row_dropper = RowDropper(minimum_missing_percentage_accepted=0.4)
    df_cleaned = forty_percent_missing_row_dropper.drop_missing_rows(df=df_with_default_score)

    print(df_cleaned)
