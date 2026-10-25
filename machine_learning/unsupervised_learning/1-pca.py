#!/usr/bin/env python3
"""Write a function that performs
PCA on tabular data using Scikit-learn.
    """
from sklearn import decomposition


def Apply_PCA(X, n_components, random_state):
    """pca function
    """
    pca = decomposition.PCA(n_components=n_components,
                            random_state=random_state)
    # Use fit_transform to get transformed data
    X_pca = pca.fit_transform(X)
    return (pca, X_pca)
