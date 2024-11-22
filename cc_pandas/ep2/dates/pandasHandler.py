from typing import Optional

import pandas as pd

from cc_pandas.ep2.dates.port import DateHandler


class PandasDateHandler(DateHandler):
    def __init__(self, dataframe: pd.DataFrame, date_column: str):
        self._dataframe = dataframe
        self._date_column = date_column

    def normalize_dates(self, date_format: str = "%Y-%m-%d") -> None:
        self._dataframe[self._date_column] = pd.to_datetime(
            self._dataframe[self._date_column], errors="coerce", format=date_format
        )

    def validate_dates(self) -> bool:
        return pd.api.types.is_datetime64_any_dtype(self._dataframe[self._date_column])

    def filter_outliers(self, start_date: Optional[str] = None, end_date: Optional[str] = None) -> pd.DataFrame:
        df_copy = self._dataframe.copy()
        filtered_df = self._filter_start_date(dataframe=df_copy, start_date=start_date)
        filtered_df = self._filter_end_date(dataframe=filtered_df, end_date=end_date)
        return filtered_df

    def _filter_start_date(self, dataframe: pd.DataFrame, start_date: str) -> pd.DataFrame:
        if start_date is None:
            return dataframe
        start = pd.to_datetime(start_date, errors="raise")
        return dataframe[dataframe[self._date_column] >= start]

    def _filter_end_date(self, dataframe: pd.DataFrame, end_date: str) -> pd.DataFrame:
        if end_date is None:
            return dataframe
        end = pd.to_datetime(end_date, errors="raise")
        return dataframe[dataframe[self._date_column] <= end]
