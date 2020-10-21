import pandas as pd

def filter_nan_rows(df, cols_to_look = None):
    df.dropna(subset=cols_to_look)
