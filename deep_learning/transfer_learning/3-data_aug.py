#!/usr/bin/env python3
"""Builds a data augmentation pipeline for transfer learning.
(Based on 2-unfreeze_top.py)"""
from tensorflow import keras as K


def build_data_augmentation():
    """Creates a Keras Sequential model of image data augmentation.

    Contains RandomFlip("horizontal"), RandomRotation(0.15),
    RandomZoom(0.15) and RandomContrast(0.1), all seeded with 42.

    Returns:
        A Keras Sequential augmentation model.
    """
    seed = 42
    model = K.Sequential()
    model.add(K.layers.RandomFlip("horizontal", seed=seed))
    model.add(K.layers.RandomRotation(0.15, seed=seed))
    model.add(K.layers.RandomZoom(0.15, seed=seed))
    model.add(K.layers.RandomContrast(0.1, seed=seed))

    return model
