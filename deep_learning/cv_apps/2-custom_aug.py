#!/usr/bin/env python3
"""Custom Albumentations augmentation for detection boxes."""

import albumentations as A
import numpy as np


def custom_aug(image, bboxes, labels):
    """Apply motion blur plus one elastic/optical distortion to an image.

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
            A.MotionBlur(blur_limit=5, p=0.9),
            A.OneOf(
                [
                    A.ElasticTransform(alpha=1, sigma=50, p=0.2),
                    A.OpticalDistortion(distort_limit=0.05, p=0.2),
                ],
                p=0.9,
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
