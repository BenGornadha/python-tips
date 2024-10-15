from typing import Dict
import pandas as pd

from cc_pandas.custom_exceptions.rename import UnknownColumnToRename


class ColumnRenamer:
    def rename(self, df: pd.DataFrame, old_name: str, new_name: str) -> pd.DataFrame:
        self._require_existing_column_name(df=df, column_name=old_name)
        return df.rename(columns={old_name: new_name})

    def _require_existing_column_name(self, df: pd.DataFrame, column_name: str) -> None:
        if column_name not in df.columns:
            raise UnknownColumnToRename(column_name=column_name)


class ColumnsRenamer:
    def __init__(self, rename_mapping: Dict[str, str]):
        self.rename_mapping = rename_mapping

    def rename(self, df: pd.DataFrame) -> pd.DataFrame:
        renamer: ColumnRenamer = ColumnRenamer()
        for old_name, new_name in self.rename_mapping.items():
            df = renamer.rename(df=df, old_name=old_name, new_name=new_name)
        return df

if __name__ == '__main__':
    df = pd.DataFrame({
        "First Name": ["Alice", "Bob", "Charlie"],
        "Last Name": ["Smith", "Johnson", "Williams"],
        "Age": [25, 30, 35]
    })

    #Si tu veux rename une seule colonne
    column_renamer = ColumnRenamer()
    df_with_prenom = column_renamer.rename(df=df,old_name="First Name",new_name="Prénom")
    print(df_with_prenom)

    print('--'*50)

    rename_mapping: Dict[str, str] = {
        "First Name": "first_name",
        "Last Name": "last_name"
    }

    renamer = ColumnsRenamer(rename_mapping=rename_mapping)
    df_renamed= renamer.rename(df=df)
    print(df_renamed)

