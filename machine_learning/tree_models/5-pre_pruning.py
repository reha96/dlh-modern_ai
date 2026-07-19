#!/usr/bin/env python3
"""Write a function that uses Scikit-learn to perform a Grid Search
for the best pre-pruning hyperparameters for a decision tree classifier.

    """


from sklearn import model_selection


def prepruning(X, y, clf):
    """   The search explores the following hyperparameters:
        criterion: "gini" or "entropy"
        max_depth: integer values in the range [2, 5)
        min_samples_leaf: integer values in the range [2, 5)
        min_samples_split: integer values in the range [2, 5)

Arguments:

    X: Input features
    y: Target labels
    clf: An untrained DecisionTreeClassifier instance

Returns:

    A dictionary containing the best combination
    of hyperparameters found during the grid search.

    """
    param_grid = {
        'criterion': ['gini', 'entropy'],
        'max_depth': list(range(2, 5)),
        'min_samples_leaf': list(range(2, 5)),
        'min_samples_split': list(range(2, 5))
    }
    # cross-validation: split data into k, train on k-1, test on 1
    grid_search = model_selection.GridSearchCV(
        estimator=clf,
        param_grid=param_grid,
        cv=5,
        scoring='accuracy'
    )
    grid_search.fit(X, y)
    return grid_search.best_params_
