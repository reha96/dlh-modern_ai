#!/usr/bin/env python3
"""
    Write a function def plot_churn_distribution(df):
    that visualizes churn class distribution:

"""
import matplotlib.pyplot as plt


def plot_churn_distribution(df):
    """

    df: pandas DataFrame with a Churn column
    Generates a bar plot of Churn value counts
    Uses colors: skyblue for ('No'), salmon for ('Yes')
    Displays the plot
    Returns: None

    """
    plt.figure(figsize=(12, 8))
    # Get counts in a specic order (No, then Yes)
    counts = df['Churn'].value_counts().reindex(['No', 'Yes'])

    plt.bar(counts.index, counts.values, color=[
            'skyblue', 'salmon']) # no label needed

    plt.ylabel("Count")
    plt.title("Churn Distribution")
    plt.show()

    return None
