#!/usr/bin/env python3
"""Builds a frozen MobileNetV2 feature extractor for transfer learning."""
from tensorflow import keras as K


def build_feature_extractor():
    """Loads MobileNetV2 without its classification head and freezes it.

    Loads MobileNetV2 with ImageNet weights and an input shape of
    (224, 224, 3) without its top classification layer, freezes the
    base model so its weights are not updated during training, and
    adds a GlobalAveragePooling2D layer on top.

    Returns:
        A Keras Model mapping input images to extracted features.
    """
    # load from TF/Keras
    input_shape = (224, 224, 3)
    
    # include top param: fully-connected layer at the top of the network
    base_m = K.applications.MobileNetV2(
        weights="imagenet", include_top=False,
        input_shape=input_shape)

    # freeze base (not trainable)
    base_m.trainable = False
    
    # add 2D avg pooling to its output
    # GlobalAveragePooling2D  reutrns  a 1D output by default vs 3D
    base_m.output = K.layers.GlobalAveragePooling2D()(base_m.output)
    model = K.Model(base_m.input, base_m.output)
    return model
