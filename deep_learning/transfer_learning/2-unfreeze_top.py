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
    # find the nested base model, or use the model itself
    base = model
    for layer in model.layers:
        if hasattr(layer, "layers"):
            base = layer
            break
    # freeze everything, then open only the last n_layers
    total = len(base.layers)
    cutoff = total - max(0, n_layers)
    if cutoff < 0:
        cutoff = 0
    for layer in base.layers[:cutoff]:
        layer.trainable = False
    for layer in base.layers[cutoff:]:
        layer.trainable = True
