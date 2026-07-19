#!/usr/bin/env python3
"""Write a function that trains multiple decision tree classifiers
over a range of cost-complexity pruning parameters (ccp_alpha)
and evaluates their performance.
    """

from sklearn import tree
train_tree = __import__('1-train').train_tree


def prune_and_evaluate_trees(X_train, y_train, X_test, y_test,
                             ccp_alphas, random_state,
                             min_samples_leaf, min_samples_split):
    """This function helps analyze how different
    pruning strengths affect model complexity and performance.

    Arguments:

    X_train, y_train: Training data and labels
    X_test, y_test: Testing data and labels
    ccp_alphas: A NumPy array of pruning alpha values to use
    for training different trees.
    random_state: Integer seed for reproducibility.
    min_samples_leaf: (int) Minimum number of samples required at
    a leaf node
    min_samples_split: (int) Minimum number of samples required to
    split an internal node

Returns:

    clfs: A list of trained DecisionTreeClassifier instances, each
    corresponding to a ccp_alpha value.
    train_scores: A list of training accuracy scores for each
    classifier.
    test_scores: A list of testing accuracy scores for each
    classifier.

    """
    clfs = []
    train_scores = []
    test_scores = []
    for alpha in ccp_alphas:
        clf = tree.DecisionTreeClassifier(
            criterion='gini', max_depth=None,
            min_samples_leaf=min_samples_leaf,
            min_samples_split=min_samples_split,
            random_state=random_state, ccp_alpha=alpha
        )
        train_tree(clf, X_train, y_train)
        clfs.append(clf)
        train_scores.append(clf.score(X_train, y_train))
        test_scores.append(clf.score(X_test, y_test))
    return clfs, train_scores, test_scores
