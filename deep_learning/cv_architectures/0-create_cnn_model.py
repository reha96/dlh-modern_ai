#!/usr/bin/env python3
"""Creates a Convolutional Neural Network (CNN) model.
(Based on supervised_learning/keras/0-sequential.py)
"""
from tensorflow import keras as K


def create_cnn_model(input_shape, filters, kernel_sizes, activations,
                     pooling_type='max'):
    """
    Creates a Convolutional Neural Network (CNN) model.

    Args:
        input_shape (tuple): the shape of the input data
            (excluding the batch size)
        filters (list): the number of filters in each convolutional layer
        kernel_sizes (list): the size of the kernels for each
            convolutional layer
        activations (list): the activation functions for each
            convolutional layer
        pooling_type (str): the type of pooling ('max' or 'avg',
            default is 'max')

    Returns:
        a compiled CNN model
    """
    # start an empty pipeline; each add() appends a filter
    model = K.Sequential()
    # one filter per entry in filters, in order
    for i in range(len(filters)):
        # add convolution 2D layer
        model.add(K.layers.Conv2D(
            filters=filters[i],
            kernel_size=kernel_sizes[i],
            activation=activations[i]))
        if pooling_type == 'max':
            model.add(K.layers.MaxPooling2D())
        else:
            model.add(K.layers.AveragePooling2D())

    # unrolls the 5×5×64 cube into 1600 numbers so Dense accepts it
    model.add(K.layers.Flatten())
    # hardcoded 10 as Fashion-MNIST has 10 classes
    model.add(K.layers.Dense(10, activation='softmax'))

    # compiled model
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy')
    return model
