#!/usr/bin/env python3
"""Write a function Standardize(X) that standardizes tabular data using Scikit-learn.
"""
from sklearn import preprocessing


def Standardize(X):
    """
    function to standardize
    """
    # extract means from all features (axis=0)
    mu = np.mean(X, axis=0)

    # extract stds as above
    sigma = np.std(X, axis=0)

    return (X-mu)/sigma
