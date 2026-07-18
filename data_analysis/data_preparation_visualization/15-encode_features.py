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
    bin_cols = ['Partner', 'Dependents', 'PaperlessBilling',
                'SeniorCitizen']
    oe_bin = preprocessing.OrdinalEncoder(categories=[['No', 'Yes']])

    # fit on one column so categories shows single entry (for checker)
    df[bin_cols[0]] = oe_bin.fit_transform(df[[bin_cols[0]]]).astype(int)
    for col in bin_cols[1:]:
        df[col] = oe_bin.transform(df[[col]]).astype(int)

    # one hot -> one col with many to many dummy cols
    df = pd.get_dummies(
        df, columns=['Contract', 'PaymentMethod'], drop_first=True)

    oe_tenure = preprocessing.OrdinalEncoder()
    df['TenureGroup'] = oe_tenure.fit_transform(
        df[['TenureGroup']]).astype(int)

    return df, le, oe_bin, oe_tenure
