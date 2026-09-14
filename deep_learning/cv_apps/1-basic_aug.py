#!/usr/bin/env python3
"""Basic Albumentations augmentation for detection boxes."""

import albumentations as A
import numpy as np


def basic_aug(image, bboxes, labels):
    """Apply flip, brightness/contrast and affine jitter to an image.

    Args:
        image: RGB image as a numpy array.
        bboxes: boxes in Pascal VOC pixel format ([x1, y1, x2, y2]).
        labels: class id per box.

    Returns:
        Tuple of augmented image array, boxes array and labels list.
    """
    # fixed seed so repeated calls give identical outputs
    transform = A.Compose(
        [
            A.HorizontalFlip(p=0.5),
            A.RandomBrightnessContrast(p=0.2),
            A.Affine(
                translate_percent=0.1,
                scale=0.1,
                rotate=[-30, 0],
                p=0.5,
            ),
        ],
        bbox_params=A.BboxParams(
            format="pascal_voc", label_fields=["labels"]),
        seed=42,
    )
    # image and boxes move together through one call
    out = transform(image=image, bboxes=list(bboxes),
                    labels=list(labels))
    # fixed array/list return types, valid even with zero boxes
    return (
        np.asarray(out["image"]),
        np.array(out["bboxes"], dtype=np.float32).reshape(-1, 4),
        list(out["labels"]),
    )
