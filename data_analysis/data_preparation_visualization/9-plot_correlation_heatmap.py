#!/usr/bin/env python3
"""
Write a function that visualizes correlations between
continuous numeric features using seaborn
"""
import seaborn as sns
import matplotlib.pyplot as plt


def plot_correlation_heatmap(df):
    """
    df: pandas DataFrame
Computes pairwise correlations
Generates an annotated heatmap with coolwarm colormap
Set vmin = -1 and vmax = 1 so that the heatmap color mapping
reflects the full correlation range
Displays the plot
Returns: None
    """
    plt.figure(figsize=(6, 5))
    df = df.select_dtypes(include='number')
    df = df.corr()
    sns.heatmap(df, vmin=-1, annot=True, vmax=1, cmap='coolwarm')
    plt.title("Correlation Matrix")
