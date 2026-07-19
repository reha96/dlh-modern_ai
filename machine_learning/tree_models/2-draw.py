#!/usr/bin/env python3
"""Write a function that displays the textual structure of a
trained decision tree classifier using Scikit-learn.
    """

from sklearn import tree


def draw(clf, feature_names, class_names):
    """Arguments:

clf: A trained DecisionTreeClassifier instance from Scikit-learn
feature_names: A list of the input feature names
class_names: A list of the target class names

Returns:
None. The function prints a readable
text representation of the decision tree structure.
    """

    tree_text = tree.export_text(
        clf,
        feature_names=list(feature_names),
        class_names=list(class_names)
    )
    print(tree_text)
