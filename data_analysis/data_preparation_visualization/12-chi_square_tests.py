#!/usr/bin/env python3
"""Write a function that performs chi-square tests
for categorical features, using SciPy:
    """

import pandas as pd
from scipy import stats


def chi_square_tests(df):
    """df: pandas DataFrame with Churn and categorical columns

Computes the Chi-square p-value to test the independence
between each categorical feature and the target variable Churn,
excluding Churn itself from the features tested.

Returns a dictionary: {feature_name: p_value}

    Args:
        df (_type_): _description_
    """
    
    df = df.select_dtypes(include="numeric")
    out = {}

    for col in df:
        table = pd.crosstab(df[col], df['Churn'])
        _, p, _, _ = stats.chi2_contingency(table)
        out[col] = p

    return out
