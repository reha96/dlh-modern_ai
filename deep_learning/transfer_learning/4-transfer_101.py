#!/usr/bin/env python3
"""Trains a transfer-learning model with callbacks and plots.
(Based on 3-augmentation.py)"""
from tensorflow import keras as K


def train_transfer_model():
    """Builds, trains and saves an image classifier with transfer learning.

    Trains on the caltech-101 dataset (101 classes + background),
    in two phases (frozen head, then fine-tuned top layers), and
    saves the model to caltech101_model.h5 (>=85% validation accuracy).
    """
    pass
