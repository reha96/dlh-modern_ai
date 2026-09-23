#!/usr/bin/env python3
"""Unfreezes top layers of a transfer-learning model for fine-tuning.
(Based on 1-classification_head.py)"""


def unfreeze_top_layers(model, n_layers):
    """Unfreezes the last n_layers of the base model.

    Unfreezes the last n_layers of the base model inside the
    transfer learning pipeline and leaves the rest frozen.

    Args:
        model: A full Keras Model with a base model as one of
            its layers.
        n_layers: Integer specifying how many of the last layers
            in the base model should be unfrozen (set as trainable).
    """
    # unfreeze
    for i in range(len(model.layers)):
        if i <= n_layers:
            model.layers[i].trainable = False
        else:
            model.layers[i].trainable = True

    # compile model
    model = model.compile()

    return model
