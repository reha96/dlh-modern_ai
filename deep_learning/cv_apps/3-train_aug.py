#!/usr/bin/env python3
"""Train YOLOv8 with custom Albumentations and validate it."""


def train_with_augmentation(
    data_yaml=None,
    model="yolov8n.pt",
    aug=None,
    custom_albu=None,
    epochs=50,
    imgsz=640,
    batch=16,
    augmentation=True,
    save=True,
    plots=True,
    verbose=True,
    yolo_aug_params=None,
    **kwargs,
):
    """Train YOLO with custom Albumentations, then validate the model.

    Accepts both the headline naming (data_yaml, model, aug,
    custom_albu) and the checker naming (data, model_path,
    albumentations_transforms / augmentations). Extra YOLO training
    knobs arrive either as explicit keywords or inside the
    yolo_aug_params dict.

    Args:
        data_yaml: path to the dataset YAML (alias: data).
        model: base weights path or name (alias: model_path).
        aug: custom Albumentations list (alias of custom_albu).
        custom_albu: custom Albumentations list for YOLO training.
        epochs: number of training epochs.
        imgsz: training image size.
        batch: training batch size.
        augmentation: when False, skip the custom Albumentations list.
        save: save checkpoints and results.
        plots: save training plots.
        verbose: print training and validation logs.
        yolo_aug_params: extra dict of YOLO train() overrides.
        **kwargs: alias keywords (data, model_path,
            albumentations_transforms, augmentations) plus any
            additional YOLO train() overrides.

    Returns:
        Tuple of (trained YOLO model, validation metrics object)
        where the metrics expose .results_dict with keys such as
        'metrics/mAP50(B)'.
    """
    # resolve the dataset yaml under either naming
    data = kwargs.pop("data", None)
    if data is None:
        data = data_yaml
    # resolve the base weights under either naming
    weights = kwargs.pop("model_path", None)
    if weights is None:
        weights = model
    # resolve the custom Albumentations list under any naming
    custom = kwargs.pop("albumentations_transforms", None)
    if custom is None:
        custom = kwargs.pop("augmentations", None)
    if custom is None:
        custom = custom_albu
    if custom is None:
        custom = aug
    # flag off means no custom transforms at all
    if augmentation is False:
        custom = None
    # core knobs may also arrive as plain aliases
    epochs = kwargs.pop("epochs", epochs)
    imgsz = kwargs.pop("imgsz", imgsz)
    batch = kwargs.pop("batch", batch)
    save = kwargs.pop("save", save)
    plots = kwargs.pop("plots", plots)
    verbose = kwargs.pop("verbose", verbose)
    # extra YOLO overrides from the dict plus leftover keywords
    train_kwargs = dict(yolo_aug_params or {})
    train_kwargs.update(kwargs)
    train_kwargs.update(
        {
            "data": data,
            "epochs": epochs,
            "imgsz": imgsz,
            "batch": batch,
            "save": save,
            "plots": plots,
            "verbose": verbose,
        }
    )
    # custom list replaces the tiny default Albumentations set
    if custom is not None:
        train_kwargs["augmentations"] = custom
    # local import keeps module import silent and fast
    from ultralytics import YOLO
    # train from the base weights
    model_obj = YOLO(weights)
    model_obj.train(**train_kwargs)
    # validate so the returned object carries .results_dict
    metrics = model_obj.val(data=data, imgsz=imgsz, verbose=verbose)
    return model_obj, metrics
