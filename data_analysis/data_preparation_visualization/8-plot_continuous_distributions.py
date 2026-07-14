#!/usr/bin/env python3
"""
Write a function that visualizes
the distributions of continuous numerical features.
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


def plot_continuous_distributions(df, columns_to_plot=None):
    """
df: pandas DataFrame

columns_to_plot: Optional list of continuous numeric columns to plot.
If None, it selects all numeric columns

For each selected column, generate:

Left subplot: Histogram with KDE using the following settings:
    bins = 30
    density = True
    alpha = 0.7
    edgecolor = 'black'
    KDE line color should be red
    Title format: "<column_name> Histogram + KDE"

Right subplot: Box Plot
    Title format: "<column_name> Boxplot"

Displays the plot

Returns: None
"""
    if columns_to_plot is None:
        df = df.select_dtypes(include="number")  # keep numeric dtype
        columns_to_plot = df.columns.to_list()
    else:
        if isinstance(columns_to_plot, str):
            columns_to_plot = [columns_to_plot]  # convert to list

    num_plots = len(columns_to_plot)

    n_cols = num_plots
    fig, axes = plt.subplots(n_cols, 2, figsize=(10, 3*n_cols))

    if n_cols == 1:
        axes = axes.reshape(1, -1)

    # Flatten the axes array to a 1D list (length = n_cols * 2)
    axes_flat = axes.flatten()

    # Loop over columns; each column uses two consecutive axes
    for i, col in enumerate(columns_to_plot):
        # The left and right axes for this column
        ax_left = axes_flat[2 * i]      # histogram + KDE
        ax_right = axes_flat[2 * i + 1]  # boxplot

        # ----- Left: Histogram + KDE -----
        ax_left.hist(df[col], bins=30, density=True,
                     alpha=0.7, edgecolor='black')

        # need to evaluate it over a range
        kde = stats.gaussian_kde(df[col])
        x_vals = np.linspace(df[col].min(), df[col].max(), 200)  # range

        ax_left.plot(x_vals, kde(x_vals), color='red', ls="--")
        ax_left.set_title(f"{col} Histogram + KDE")

        # ----- Right: Boxplot -----
        ax_right.boxplot(df[col], orientation='horizontal')
        ax_right.set_title(f"{col} Boxplot")

    # Hide any unused subplots (beyond the first num_plots*2)
    total_subplots = n_cols * 2
    for j in range(2 * num_plots, total_subplots):
        axes_flat[j].axis('off')

    plt.tight_layout()
    plt.savefig("Task_8.png")
    plt.show()
