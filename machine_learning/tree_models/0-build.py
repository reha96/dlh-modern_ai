#!/usr/bin/env python3
"""Write a function to create a decision tree
classifier using Scikit-learn.
    """
from sklearn import tree


def build_decision_tree(min_samples_leaf, min_samples_split, random_state):
    """The decision tree uses the Gini impurity measure
    to evaluate the quality of splits.
No maximum depth is set, allowing the tree to grow until
all leaves are pure or other stopping criteria are met.

Arguments:

min_samples_leaf: Minimum number of samples
required to be at a leaf node.
min_samples_split: Minimum number of samples
required to split an internal node.
random_state: Seed used by the random number
generator for reproducibility.

Returns:

model: A Scikit-learn DecisionTreeClassifier instance.

    Args:
        min_samples_leaf (_type_): _description_
        min_samples_split (_type_): _description_
        random_state (_type_): _description_
    """
    model = tree.DecisionTreeClassifier(
        criterion='gini',
        max_depth=None,
        min_samples_leaf=min_samples_leaf,
        min_samples_split=min_samples_split,
        random_state=random_state
    )
    return model
