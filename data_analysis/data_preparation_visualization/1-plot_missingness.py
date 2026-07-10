#!/usr/bin/env python3
"""
Write a function def plot_missingness(df):
that visualizes missing values in a DataFrame
"""
import matplotlib.pyplot as plt
import numpy as np


def plot_missingness(df):
    """
    visualizes missing values in a DataFrame
    """
    plt.figure(figsize=(12, 8))

    row_idx, col_idx = np.where(df.isnull().values)
    plt.scatter(row_idx, col_idx, marker="|")
    plt.yticks(range(len(df.columns)), df.columns)
    plt.title('Missingness Plot')

    plt.tight_layout()
    plt.show()
