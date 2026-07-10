#!/usr/bin/env python3
"""
Write a function def clean_total_charges(df, method='drop')
"""


def clean_total_charges(df, method='drop'):
    """handles missing values in TotalCharges

    Args:
        df (_type_): _description_
        method (str, optional): _description_. Defaults to 'drop'.
    """
    out = df.copy()
    if method == 'drop':
        out = df.dropna(subset=['TotalCharges'])  # only for said col
        return out
    elif method == 'median':
        out['TotalCharges'] = df['TotalCharges'].fillna(
            df['TotalCharges'].median())
        return out
    elif method == 'impute':
        out['TotalCharges'] = df['TotalCharges'].fillna(
            df['MonthlyCharges'] * df['tenure'])
        return out
