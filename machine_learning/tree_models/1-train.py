#!/usr/bin/env python3
"""Write a function to train a tree-based classifier using Scikit-learn.

    """


def train_tree(clf, X, y):
    """Arguments:

    clf: A Scikit-learn classifier instance
    X: Input features
    y: Target labels

Returns:

    None
    """
    clf.fit(X, y)
