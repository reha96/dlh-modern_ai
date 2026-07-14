#!/usr/bin/env python3
"""Write a function def remove_duplicates(df)
that removes duplicate rows:
"""


def remove_duplicates(df):
    """df: pandas DataFrame to process
Drops all duplicate rows
Returns the deduplicated DataFrame

    Args:
        df (_type_): _description_
    """
    df = df.drop_duplicates()
    return df
