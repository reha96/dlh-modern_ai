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
    # normalize empty params
    if optimizer_params is None:
        optimizer_params = {}

    # explicit optimizer selection
    name = optimizer_name.lower()
    if name == "adam":
        optimizer = K.optimizers.Adam(**optimizer_params)
    elif name == "sgd":
        optimizer = K.optimizers.SGD(**optimizer_params)
    elif name == "rmsprop":
        optimizer = K.optimizers.RMSprop(**optimizer_params)

    # select loss suitable to one-hot labels vs sparse (integer labels)
    # val_accuracy metric required
    model.compile(optimizer=optimizer,
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

    # train and return history obj
    history = model.fit(x_train, y_train,
                        epochs=epochs,
                        batch_size=batch_size,
                        validation_data=(x_val, y_val),
                        verbose=2)

    return model, history
