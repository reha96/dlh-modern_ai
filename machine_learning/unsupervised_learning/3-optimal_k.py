#!/usr/bin/env python3
"""Write a function that evaluates K-Means clustering
quality using silhouette scores to measure cluster cohesion
and separation, and to compute the inertia to be used
for the elbow method.
"""
from sklearn import metrics
K_Means = __import__('2-k_means').K_Means


def optimal_k(X, max_clusters, random_state):
    """find optimal k"""

    