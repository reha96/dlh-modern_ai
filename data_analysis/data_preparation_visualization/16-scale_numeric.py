#!/usr/bin/env python3
"""Write a function that standardizes numeric columns
    """

from sklearn import preprocessing


def scale_numeric(df):
    """    df: pandas DataFrame

    Scales MonthlyCharges and TotalCharges using
    StandardScaler (mean=0, std=1)

    Returns the modified DataFrame

    Args:
        df (_type_): _description_
    """

    scaler = preprocessing.StandardScaler()
    cols = ['MonthlyCharges', 'TotalCharges']
    df[cols] = scaler.fit_transform(df[cols])
    return df
