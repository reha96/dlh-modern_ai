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
    base_model = K.applications.Xception(
        weights="imagenet",
        include_top=False
    )

    base_model.trainable = False

    inputs = K.Input()
    x = base_model(training=False)
    x = K.layers.GlobalAveragePooling2D()(x)
    x = K.layers.Dropout(0.2)(x)
    outputs = K.layers.Dense(102, activation="softmax")(x)
    model = K.Model(inputs, outputs)

    callbacks = [
        K.callbacks.ModelCheckpoint(
            "best.weights.h5",
            monitor="val_accuracy",
            mode="max",
            save_best_only=True,
            save_weights_only=True,
        ),
        K.callbacks.EarlyStopping(
            monitor="val_accuracy",
            mode="max",
            patience=3,
            restore_best_weights=True,
        ),
        K.callbacks.ReduceLROnPlateau(
            monitor="val_loss",
            factor=0.2,
            patience=2,
            min_lr=1e-7,
        ),
    ]

    # Phase 1: train the new classification head.
    model.compile(
        optimizer=K.optimizers.Adam(learning_rate=1e-3),
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"],
    )

    # Phase 2: unfreeze the later Xception layers and fine-tune gently.
    base_model.trainable = True
    for layer in base_model.layers[:56]:
        layer.trainable = False
    # Keep BatchNormalization layers frozen for more stable fine-tuning.
    for layer in base_model.layers:
        if isinstance(layer, K.layers.BatchNormalization):
            layer.trainable = False

    model.compile(
        optimizer=K.optimizers.Adam(learning_rate=1e-5),
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"],
    )
