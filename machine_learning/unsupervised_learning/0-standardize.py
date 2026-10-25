#!/usr/bin/env python3
"""Write a function Standardize(X) that standardizes tabular data using Scikit-learn.
"""
from sklearn import preprocessing


def Standardize(X):
    """
    function to standardize
    """
    scaler = preprocessing.StandardScaler()
    return scaler.fit(X)
