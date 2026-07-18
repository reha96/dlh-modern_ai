#!/usr/bin/env python3
"""Write a function that splits data into train/test sets:
    """

from sklearn import model_selection


def split_data(df, target='Churn', test_size=0.2, random_state=42):
    """df: pandas DataFrame
target: Name of target column
test_size: Proportion for test split
random_state: Random seed
Uses stratified sampling to preserve class distribution
Returns: (X_train, X_test, y_train, y_test)

    Args:
        df (_type_): _description_
        target (str, optional): _description_. Defaults to 'Churn'.
        test_size (float, optional): _description_. Defaults to 0.2.
        random_state (int, optional): _description_. Defaults to 42.
    """

    X = df.drop(columns=[target])
    y = df[target]
    X_train, X_test, y_train, y_test = model_selection.train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y)
    return X_train, X_test, y_train, y_test
