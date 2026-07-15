#!/usr/bin/env python3
"""Write a function that visualizes churn rates per category:
"""
import matplotlib.pyplot as plt


def plot_categorical_vs_churn(df, col):
    """df: pandas DataFrame with Churn column
col: Categorical column name
Uses a figure size of (12, 8)
Adds a title to the plot in the format: "Churn Rate by <col>"
Plots churn rate (Yes proportion) per category as a bar plot
Sets y-axis label to "Churn Rate"
Rotates the x-axis labels by 45°
Displays the plot
Returns: None

    Args:
        df (_type_): _description_
        col (_type_): _description_
    """

    plt.figure(figsize=(12, 8))
    # Compute proportion of 'Yes' per category
    churn_rate = df.groupby(col)['Churn'].apply(lambda x: (x == 'Yes').mean())

    # Create the bar plot

    plt.bar(churn_rate.index, churn_rate.values)

    # Titles and labels
    plt.title(f"Churn Rate by {col}")
    plt.ylabel("Churn Rate")
    plt.xticks(rotation=45)

    # Display
    plt.tight_layout()
    plt.show()
