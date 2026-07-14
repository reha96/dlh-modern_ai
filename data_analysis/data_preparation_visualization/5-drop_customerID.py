#!/usr/bin/env python3
"""Write a function def drop_customerID(df):
that removes the customerID column since unique
identifiers lack predictive value:
"""


def drop_customerID(df):
    """df: pandas DataFrame containing a customerID column
Drops the customerID column
Returns the modified DataFrame

    Args:
        df (_type_): _description_
    """

    df = df.drop("customerID", axis=1)
    return df
