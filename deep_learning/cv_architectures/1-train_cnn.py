#!/usr/bin/env python3
"""Trains a CNN model.
(Based on 0-create_cnn_model.py)
"""
from tensorflow import keras as K


def compile_and_train_cnn(model, epochs, batch_size, x_train, y_train,
                          x_val, y_val, optimizer_name='adam',
                          optimizer_params=None):
    """
    Trains a CNN model.

    Args:
        model: The CNN model to be trained
        epochs (int): the number of training epochs
        batch_size (int): the size of the batches for training
        x_train: the training input data
        y_train: the training target data
        x_val: the validation input data
        y_val: the validation target data
        optimizer_name (str): the name of the optimizer to use
            (default is 'adam')
        optimizer_params (dict): additional parameters for the
            optimizer (default is None)

    Returns:
        the trained CNN model, training history object
    """
    pass
