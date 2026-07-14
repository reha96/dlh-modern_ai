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
        columns_to_plot = df.columns.to_list()
    else:
        if isinstance(columns_to_plot, str):
            columns_to_plot = [columns_to_plot]  # convert to list

    num_plots = len(columns_to_plot)
    n_cols, n_rows = 3, (num_plots+2)//3   # dynamic for any graph

    fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 5*n_rows))

    # Flatten axes to a 1D array, else to list
    axes = axes.flatten() if hasattr(axes, 'flatten') else [axes]

    # 2. Plot using ax.bar (not pandas .plot)
    for ax, col in zip(axes, columns_to_plot):
        counts = df[col].value_counts()
        ax.bar(counts.index, counts.values)
        ax.set_title(col)
        ax.tick_params(axis='x', labelrotation=45)

    # 3. Hide unused subplots do not use .delaxes(axes[j])
    for ax in axes[num_plots:]:
        ax.axis('off')

    plt.tight_layout()
    plt.savefig("Task_7.png")
    plt.show()
