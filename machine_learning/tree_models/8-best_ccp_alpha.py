#!/usr/bin/env python3
"""Write a function that selects the best pruning value ccp_alpha
for a set of trained decision trees.
    """


def get_best_alpha(clfs, train_scores, test_scores, ccp_alphas):
    """
    This function first identifies the model(s) that achieve
    the highest test accuracy.
    If multiple models share this same test accuracy, it selects
    the one with the smallest difference between training and
    test accuracy to favor better generalization.
    In the event of a further tie, the model associated
    with the largest ccp_alpha is chosen to promote a simpler,
    more regularized tree.

Arguments:

    clfs: List of trained DecisionTreeClassifier instances,
    each trained with a different ccp_alpha.
    train_scores: List of training accuracy scores corresponding
    to each classifier in clfs.
    test_scores: List of test accuracy scores corresponding
    to each classifier in clfs as well.
    ccp_alphas: List or array of ccp_alpha values used to
    train the classifiers.

Returns:

    best_alpha: The most appropriate ccp_alpha value based
    on test accuracy and generalization.
    best_clf: The trained classifier associated with
    the best alpha.

    """
    # Tier 1: highest test accuracy
    max_test = max(test_scores)
    candidates = [i for i, s in enumerate(test_scores) if s == max_test]

    if len(candidates) > 1:
        # Tier 2: smallest train-test gap (best generalization)
        gaps = [abs(train_scores[i] - test_scores[i]) for i in candidates]
        min_gap = min(gaps)
        candidates = [i for i, g in zip(candidates, gaps) if g == min_gap]

    if len(candidates) > 1:
        # Tier 3: largest ccp_alpha (simplest tree)
        best_idx = max(candidates, key=lambda i: ccp_alphas[i])
    else:
        best_idx = candidates[0]

    return ccp_alphas[best_idx], clfs[best_idx]
