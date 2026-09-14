#!/usr/bin/env python3
"""Custom Albumentations augmentation for detection boxes."""

import random

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
    # tolerate None, scalar labels and flat single-box inputs
    if bboxes is None:
        bboxes = []
    if labels is None:
        labels = []
    if isinstance(labels, (str, bytes)):
        labels_in = [labels]
    else:
        try:
            labels_in = list(labels)
        except TypeError:
            labels_in = [labels]
    boxes_in = list(bboxes)
    # wrap a flat [x1, y1, x2, y2] single box into one row
    if len(boxes_in) == 4 and all(
            isinstance(v, (int, float, np.generic)) for v in boxes_in):
        boxes_in = [boxes_in]
    # seed 42 inside the call so repeats are identical
    random.seed(42)
    np.random.seed(42)
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
    # Compose(seed=...) clones one seed into each child, so every
    # child shares a first draw (Random(42) -> 0.6394) and seed 42
    # parks all p-gates on the same answer. Give each child its
    # own 42-based stream instead (OneOf spreads it to its kids).
    for index, child in enumerate(transform.transforms):
        child.set_random_seed(42 + index)
    # image and boxes move together through one call
    out = transform(image=image, bboxes=boxes_in, labels=labels_in)
    # albumentations casts int label lists to float; restore ints
    out_labels = list(out["labels"])
    if labels_in and all(
            isinstance(v, (int, np.integer)) and not isinstance(v, bool)
            for v in labels_in):
        fixed = []
        for v in out_labels:
            if isinstance(v, float) and v.is_integer():
                fixed.append(int(v))
            elif isinstance(v, np.floating) and float(v).is_integer():
                fixed.append(int(v))
            elif isinstance(v, np.integer):
                fixed.append(int(v))
            else:
                fixed.append(v)
        out_labels = fixed
    # fixed array/list return types, valid even with zero boxes
    return (
        np.asarray(out["image"]),
        np.array(out["bboxes"], dtype=np.float32).reshape(-1, 4),
        out_labels,
    )
