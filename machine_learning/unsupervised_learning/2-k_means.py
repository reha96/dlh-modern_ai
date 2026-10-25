#!/usr/bin/env python3
"""Write a function that creates and
fits a K-Means clustering model using
Scikit-learn on tabular data.
    """
from sklearn import cluster


def K_Means(X, n_clusters, random_state):
    """function K_Means
    """
    k_means = cluster.KMeans(n_clusters=n_clusters,
                             random_state=random_state).fit(X)
    return (k_means)
