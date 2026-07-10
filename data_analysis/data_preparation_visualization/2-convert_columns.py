#!/usr/bin/env python3
"""Write a function def convert_columns(df):
that performs type conversion for specific columns
    """

import pandas as pd


def convert_columns(df):
    """performs type conversion for specific columns

    Args:
        df (_type_): _description_
    """
    df['TotalCharges'] = pd.to_numeric(
        # coerce converts non-numeric to NaN
        df['TotalCharges'], errors='coerce')
    df['SeniorCitizen'] = df['SeniorCitizen'].replace(
        {
            0: 'No',
            1: 'Yes'
        }
    )  # replace leaves un-mapped values as is
    return df
