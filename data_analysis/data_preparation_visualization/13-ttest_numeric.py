#!/usr/bin/env python3
"""Write a function that performs Welch's t-tests for continuous numeric features using scipy
"""

from scipy import stats


def ttest_numeric(df):
    """df: pandas DataFrame with Churn column

Computes t-test p-value comparing Churn=Yes vs Churn=No
for each numeric feature

The Hypothesis being tested is:

H₀ (null): The means of the variable are equal
in Churn=Yes and Churn=No groups
H₁ (alternative): The means differ significantly

Returns a dictionary: {feature_name: p_value}

    Args:
        df (_type_): _description_
    """
    out = {}
    num_cols = df.select_dtypes(include="number").columns  # keep numeric
    for col in num_cols:
        yes = df[df['Churn'] == 'Yes'][col]  # keep yes rows
        no = df[df['Churn'] == 'No'][col]  # keep no rows
        _, p = stats.ttest_ind(yes, no)  # check mean
        out[col] = p  # store in dict
    return out
