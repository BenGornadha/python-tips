import pandas as pd

from cc_pandas.missing_values.missing_value import MissingValueFiller
from cc_pandas.missing_values.strategy import MeanStrategy, MedianStrategy

if __name__ == '__main__':
    df = pd.DataFrame({
        "Name": ["Alice", "Bob", "Charlie", None],
        "Age": [25, 30, None, 35],
        "Score": [85, None, 90, None],
    })

    mean_filler = MissingValueFiller(strategy=MeanStrategy())
    df_with_mean = mean_filler.apply(df=df, column='Age')
    df_with_mean = mean_filler.apply(df=df_with_mean, column='Score')

    median_filler = MissingValueFiller(strategy=MedianStrategy())
    df_with_median = median_filler.apply(df=df_with_mean, column='Score')

    print(df_with_median)
