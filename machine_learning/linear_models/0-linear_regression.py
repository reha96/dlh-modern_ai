#!/usr/bin/env python3

"""Write a function to create a linear regression model.
"""

from sklearn import linear_model


def Linear_Regression():
    """using Scikit-learn, use the ordinary least squares to
fit a linear model to the data

Arguments:

None
Returns:

model: An untrained LinearRegression instance.

    """
    reg = linear_model.LinearRegression()
    return reg
