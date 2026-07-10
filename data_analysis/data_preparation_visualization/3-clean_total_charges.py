#!/usr/bin/env python3
"""
Write a function def clean_total_charges(df, method='drop')
"""
import pandas as pd


def clean_total_charges(df, method='drop'):
    """handles missing values in TotalCharges

    Args:
        df (_type_): _description_
        method (str, optional): _description_. Defaults to 'drop'.
    """
    if method == 'drop':
        df = df.dropna(subset=['TotalCharges'])  # only for said col
    elif method == 'median':
        df['TotalCharges'] = df['TotalCharges'].fillna(
            df['TotalCharges'].median())
    elif method == 'impute':
        df['TotalCharges'] = df['TotalCharges'].fillna(
            df['MonthlyCharges'] * df['tenure'])

    return df
