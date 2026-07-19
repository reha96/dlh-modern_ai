#!/usr/bin/env python3
"""Write a function that computes and returns the feature importances
with a trained random forest model.
    """
import numpy as np


def feature_importance(rf):
    """Arguments:

    rf: A trained Scikit-learn RandomForestClassifier instance.

Returns:

    importances: A NumPy array of feature importance scores.
    indices: A NumPy array of feature indices sorted from least
    to most important (ascending order).

    """
    importances = rf.feature_importances_
    indices = np.argsort(importances)
    return importances, indices
