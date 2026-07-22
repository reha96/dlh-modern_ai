#!/usr/bin/env python3
"""Write a function that helps generate model explanations
using the SHAP library.
    """

import shap


def get_shap_explainer_and_values(model, X_train, X_test):
    """Create a SHAP explainer using X_train as the background dataset
Compute SHAP values for X_test
Arguments:

model: A trained regression model
X_train: Input data used to initialize the explainer
X_test: Input data to explain
Returns:

explainer: SHAP explainer object
shap_values: SHAP values for the predictions on X_test
    """
    explainer = shap.LinearExplainer(model, X_train)
    shap_values = explainer(X_test)
    return explainer, shap_values
