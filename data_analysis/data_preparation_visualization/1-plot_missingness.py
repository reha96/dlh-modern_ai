#!/usr/bin/env python3
"""
"""
import matplotlib.pyplot as plt


def plot_missingness(df):
    """
    """
    plt.figure(figsize=(12, 8))

    plt.scatter(df.isna().sum(), df.columns, marker="|")

    plt.tight_layout()
    plt.show()
