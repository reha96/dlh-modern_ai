#!/usr/bin/env python3
"""Write a function that retrieves the cost-complexity pruning path
for a given decision tree classifier.
    """


def get_pruning_path(clf, X, y):
    """
    Arguments:

    clf: A DecisionTreeClassifier instance
    X: Input features
    y: Target labels

Returns:

    ccp_alphas: A NumPy array containing the effective alpha
    values used for pruning
    impurities: A NumPy array containing the total impurity
    of leaves at each corresponding alpha

    """
    path = clf.cost_complexity_pruning_path(X, y)
    return path.ccp_alphas, path.impurities
