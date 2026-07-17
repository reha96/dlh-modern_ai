#!/usr/bin/env python3
"""Write a function that engineers new features from the dataset
    """


import pandas as pd


def create_features(df):
    """df: pandas DataFrame

NumServices: Number of services the customer is subscribed to
(counting only those with 'Yes' in selected service-related columns)

Do not include the PhoneService column, as it was dropped
based on the decision made in Task 12

For InternetService, count 'DSL' and 'Fiber optic' as 'Yes'
(i.e., subscribed to the service), and 'No' as not subscribed

TenureGroup: A categorical column
that bins the tenure into intervals: 0-12, 13-24, 25-48, 49-60, 60+ ,
where 0 is excluded and upper bounds are inclusive.

Drops the original columns that were used to create the new ones

Returns the modified DataFrame

    Args:
        df (_type_): _description_
    """
    df = df[df["InternetService"]== 'Yes']
    df.describe()
    
    

plot_numeric_vs_churn = __import__(
    '11-plot_numeric_vs_churn').plot_numeric_vs_churn


df = pd.read_csv(
    '/home/rehat/Documents/GitHub/dlh-modern_ai/data_analysis/data_preparation_visualization/precleaned-Telco-Customer-Churn.csv')
df.drop(columns=['gender', 'PhoneService'], inplace=True)
df = create_features(df)
plot_numeric_vs_churn(df, 'NumServices')
