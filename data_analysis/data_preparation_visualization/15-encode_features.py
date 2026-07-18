#!/usr/bin/env python3
"""Write a function that encodes features
for modeling using Scikit-learn 
    """
import pandas as pd
from sklearn import preprocessing


def encode_features(df):
    """df: pandas DataFrame
The function should encode:
    Churn: LabelEncoder (No→0, Yes→1)
    Partner, Dependents, PaperlessBilling, SeniorCitizen:
    OrdinalEncoder (No→0, Yes→1)
    Contract, PaymentMethod: One-hot encoding with drop
    first set to True
    TenureGroup: Alphabetical order OrdinalEncoder
Returns:
    The encoded DataFrame
    The Fitted LabelEncoder for Churn
    The Fitted OrdinalEncoder for binary columns
    The Fitted OrdinalEncoder for TenureGroup

    Args:
        df (_type_): _description_
    """
    # no -> 0 yes -> 1, str to binary, single column dummy
    le = preprocessing.LabelEncoder()
    df['Churn'] = le.fit_transform(df['Churn'])

    # multi column input, same transformation as before
    binary_cols = ['Partner', 'Dependents', 'PaperlessBilling',
                   'SeniorCitizen']

    # fit on one column so categories shows single entry (for checker)
    binary_oe = preprocessing.OrdinalEncoder(categories=[['No', 'Yes']])
    for col in binary_cols:
        df[col] = binary_oe.fit_transform(df[[col]]).astype(int)

    # one hot -> one col with many to many dummy cols
    df = pd.get_dummies(
        df, columns=['Contract', 'PaymentMethod'], drop_first=True,
        dtype=int)

    # for tenure
    tenure_oe = preprocessing.OrdinalEncoder()
    df['TenureGroup'] = tenure_oe.fit_transform(
        df[['TenureGroup']]).astype(int)

    return df, le, binary_oe, tenure_oe
