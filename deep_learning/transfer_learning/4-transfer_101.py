#!/usr/bin/env python3
"""Trains a transfer-learning model on Caltech-101.
(Based on 3-data_aug.py)"""
from pathlib import Path

import tensorflow as tf
from tensorflow import keras as K


def train_transfer_model():
    """Builds, trains and saves an image classifier with transfer learning.

    Trains on the caltech-101 dataset (101 classes + background),
    in two phases (frozen head, then fine-tuned top layers), and
    saves the model to caltech101_model.h5 (>=85% validation accuracy).
    """
    DATA_DIR = (Path(__file__).resolve().parent
                / "caltech-101" / "101_ObjectCategories")
    IMAGE_SIZE = (224, 224)
    BATCH_SIZE = 32
    SEED = 42

    # Load folders as training and validation datasets.
    train_ds = K.utils.image_dataset_from_directory(
        DATA_DIR,
        validation_split=0.2,
        subset="training",
        seed=SEED,
        image_size=IMAGE_SIZE,
        batch_size=BATCH_SIZE,
        label_mode="int",
    )
    valid_ds = K.utils.image_dataset_from_directory(
        DATA_DIR,
        validation_split=0.2,
        subset="validation",
        seed=SEED,
        image_size=IMAGE_SIZE,
        batch_size=BATCH_SIZE,
        label_mode="int",
    )

    num_classes = len(train_ds.class_names)
    print(f"Found {num_classes} classes")

    # Xception expects its inputs to be preprocessed to the range [-1, 1].
    preprocess = K.layers.Lambda(
        K.applications.xception.preprocess_input,
        name="xception_preprocess",
    )

    train_ds = train_ds.shuffle(1000, seed=SEED).prefetch(
        tf.data.AUTOTUNE
    )
    valid_ds = valid_ds.prefetch(tf.data.AUTOTUNE)

    # Augmentation is active only during training.
    augmentation = K.Sequential([
        K.layers.RandomFlip("horizontal", seed=SEED),
        K.layers.RandomRotation(0.15, seed=SEED),
        K.layers.RandomZoom(0.15, seed=SEED),
        K.layers.RandomContrast(0.1, seed=SEED),
    ], name="data_augmentation")

    base_model = K.applications.Xception(
        weights="imagenet",
        include_top=False,
        input_shape=(*IMAGE_SIZE, 3),
    )
    base_model.trainable = False

    inputs = K.Input(shape=(*IMAGE_SIZE, 3))
    x = augmentation(inputs)
    x = preprocess(x)
    x = base_model(x, training=False)
    x = K.layers.GlobalAveragePooling2D()(x)
    x = K.layers.Dropout(0.2)(x)
    outputs = K.layers.Dense(num_classes, activation="softmax")(x)
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
    model.fit(
        train_ds,
        validation_data=valid_ds,
        epochs=10,
        callbacks=callbacks,
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
    model.fit(
        train_ds,
        validation_data=valid_ds,
        epochs=20,
        callbacks=callbacks,
    )

    # Restore the checkpoint with the best validation accuracy.
    model.load_weights("best.weights.h5")
    model.save("caltech101_model.h5")


if __name__ == "__main__":
    train_transfer_model()
