#!/usr/bin/env python3
"""Write a function to create a logistic regression model
using Scikit-learn.
    """
from sklearn import linear_model


def Logistic_Regression_Model(random_state):
    """Performs binary classification
by fitting a logistic function.

    Arguments:

random_state: An integer used to set the random seed for reproducibility.
Returns:

model: An untrained LogisticRegression instance.
    """

    model = linear_model.LogisticRegression(random_state=random_state)
    return model
