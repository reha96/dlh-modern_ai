#!/usr/bin/env python3
"""Attaches a custom classification head to a pretrained feature extractor.
(Based on 0-frozen_extractor.py)"""
from tensorflow import keras as K


def add_classification_head(base_model, num_classes):
    """Attaches a custom classification head to a feature extractor.

    Takes the pooled feature vector output of a pretrained base model,
    adds a dense layer with 128 units and relu activation, and adds a
    final classification layer.

    Args:
        base_model: A Keras Model whose output is a pooled feature vector.
        num_classes: An integer representing the number of output classes.

    Returns:
        A new Keras Model ready for classification.
    """
    pass
