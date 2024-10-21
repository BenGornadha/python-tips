import pandas as pd

from cc_pandas.clean_columns.clean_columns import ColumnsCleaner
from cc_pandas.droppers.droppers import RowDropper, ColumnDropper
from cc_pandas.missing_values.missing_value import MissingValueFiller
from cc_pandas.missing_values.strategy import MeanStrategy, MedianStrategy

if __name__ == '__main__':
    df = pd.DataFrame({
        "First-Name": ["Alice", "Bob", "Charlie"],
        "Last Name": ["Smith", "Johnson", "Williams"],
        "Age": [25, 30, 35],
        "Score": [85, None, 90],
        "Email Address": ["alice@example.com", "bob@example.com", "charlie@example.com"],
        "Phone Number": ["555-1234", "555-5678", "555-9876"]
    })
    df_snake_case = ColumnsCleaner.all_to_snake_case(df=df)

    half_missing_row_dropper = RowDropper(maximum_missing_percentage_accepted=0.5)
    df_missing_row_cleaned = half_missing_row_dropper.drop(df=df)

    half_missing_column_dropper = ColumnDropper(maximum_missing_percentage_accepted=0.5)
    df_cleaned = half_missing_column_dropper.drop(df=df_missing_row_cleaned)

    mean_filler = MissingValueFiller(strategy=MeanStrategy())
    df_with_mean = mean_filler.apply(df=df_cleaned, column='Age')
    df_with_mean = mean_filler.apply(df=df_with_mean, column='Score')

    median_filler = MissingValueFiller(strategy=MedianStrategy())
    df_with_median = median_filler.apply(df=df_with_mean, column='Score')
