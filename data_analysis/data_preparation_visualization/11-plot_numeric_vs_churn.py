#!/usr/bin/env python3
"""Write a function that compares
continuous numeric feature distributions by churn:
    """
import matplotlib.pyplot as plt


def plot_numeric_vs_churn(df, col):
    """df: pandas DataFrame with Churn column
col: Numeric column name
Uses a figure size of (12, 8)
Adds a title to the plot in the format: "<col> Distribution by Churn"
Plots overlapping histograms for Churn=Yes and Churn=No
Sets the x-axis label to "<col>"
Uses 30 bins to group the data along the x-axis
Adds a legend with a title
Displays the plot
Returns: None

    Args:
        df (_type_): _description_
        col (_type_): _description_
    """
    plt.figure(figsize=(12, 8))

    # split data into 2 groups
    yes = df[df['Churn'] == 'Yes'][col]
    no = df[df['Churn'] == 'No'][col]

    # plot overlapping
    plt.hist([no, yes], bins=30, label=['No', 'Yes'])

    plt.title(f"{col} Distribution by Churn")
    plt.xlabel(col)
    plt.legend(title='Churn')
    plt.show()
