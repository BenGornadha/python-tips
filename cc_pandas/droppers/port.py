from abc import ABC

import pandas as pd


class Dropper(ABC):

    def _require_non_empty_dataframe(self, df: pd.DataFrame):
        if df.empty:
            raise ValueError("The DataFrame is empty. Nothing to drop.")


    def drop(self, df: pd.DataFrame):
        raise NotImplementedError