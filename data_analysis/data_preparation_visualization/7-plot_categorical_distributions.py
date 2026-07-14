#!/usr/bin/env python3
"""
Write a function that visualizes categorical feature distributions
"""
import matplotlib.pyplot as plt


def plot_categorical_distributions(df, columns_to_plot=None):
    """
    df: pandas DataFrame
    columns_to_plot: Optional list of categorical columns
    (Default: all columns with dtype object, excluding
    the target variable Churn.)
    Generates bar plots for each categorical feature in a grid layout
    Rotates x-axis labels by 45°
    Displays the plot
    Returns: None
    """

    if columns_to_plot is None:
        df = df.drop("Churn", axis=1)  # remove target, assume
        df = df.select_dtypes(include="object")  # keep object dtype
    else:
        pass
    n_cols, n_rows = 3, 6  # get dims from example plot
    num_plots = df.shape[1]

    fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 5*n_rows))

    # Flatten axes to a 1D array, even if it's already 1D or 2D
    axes = axes.flatten()

    for i, col in enumerate(df.columns):
        # Plot on the i-th subplot
        df[col].value_counts().plot(kind='bar', ax=axes[i])
        axes[i].set_title(col)
        axes[i].tick_params(axis='x', rotation=45)
        axes[i].set_xlabel('')  # remove x-axis

    # Hide any unused subplots (if num_plots < rows*cols space)
    for j in range(num_plots, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.savefig("Task_7.png")
    plt.show()
