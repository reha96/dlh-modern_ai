#!/usr/bin/env python3
"""Write a function that creates and
fits a K-Means clustering model using
Scikit-learn on tabular data.
    """
from sklearn import cluster


def K_Means(X, n_clusters, random_state):
    """function K_Means
    """
    k_means = cluster.k_means(X, n_clusters=n_clusters,
                              random_state=random_state)
    return (k_means)
