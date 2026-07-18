#!/usr/bin/env python3
"""Write a function that engineers new features from the dataset
    """


import pandas as pd


def create_features(df):
    """df: pandas DataFrame

NumServices: Number of services the customer is subscribed to
(counting only those with 'Yes' in selected service-related columns)

Do not include the PhoneService column, as it was dropped
based on the decision made in Task 12

For InternetService, count 'DSL' and 'Fiber optic' as 'Yes'
(i.e., subscribed to the service), and 'No' as not subscribed

TenureGroup: A categorical column
that bins the tenure into intervals: 0-12, 13-24, 25-48, 49-60, 60+ ,
where 0 is excluded and upper bounds are inclusive.

Drops the original columns that were used to create the new ones

Returns the modified DataFrame

    Args:
        df (_type_): _description_
    """
    services = ['OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
                'TechSupport', 'StreamingTV', 'StreamingMovies']

    df = pd.DataFrame(df[services])  # to access function helpers, DF
    # Count 'Yes' across service columns
    df['NumServices'] = (df[services] == 'Yes').sum(axis=1)
    # Add 1 if InternetService is DSL or Fiber optic
    df['NumServices'] += df['InternetService'].isin(
        ['DSL', 'Fiber optic']).astype(int)
    # pd.cut is the standard way to create bins
    bins = [0, 12, 24, 48, 60,  df['tenure'].max() + 1]
    labels = ['0-12', '13-24', '25-48', '49-60', '60+']
    df['TenureGroup'] = pd.cut(df['tenure'], bins=bins, labels=labels,
                               right=True, include_lowest=False)
    return df
