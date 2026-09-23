#!/usr/bin/env python3
"""Unfreezes top layers of a transfer-learning model for fine-tuning.
(Based on 1-classification_head.py)"""
from tensorflow import keras as K


def fine_tune_model(model, num_unfreeze, learning_rate=1e-5):
    """Fine-tunes a transfer-learning model by unfreezing its top layers.

    Unfreezes the top layers of the pretrained base inside the model
    and recompiles the model with a low learning rate for fine-tuning.

    Args:
        model: A Keras Model built on a frozen pretrained base.
        num_unfreeze: An integer representing the number of top base
            layers to unfreeze.
        learning_rate: A float representing the learning rate to use
            for fine-tuning.

    Returns:
        The recompiled Keras Model ready for fine-tuning.
    """
    # unfreeze
    for layer in model.layers[num_unfreeze:]:
        layer.trainable = True

    # compile model
    optimizer = K.optimizers.SGD(learning_rate=learning_rate)
    model.compile(loss="sparse_categorical_crossentropy", optimizer=optimizer,
                  metrics=["accuracy"])
    return model
