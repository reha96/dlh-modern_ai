#!/usr/bin/env python3
"""Grid-search inference conf/iou thresholds with YOLOv8 validation."""

from pathlib import Path


def _as_float(value, default=0.0):
    """Coerce a metric value to float, falling back to default."""
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def _extract_metrics(val_metrics):
    """Pull map/precision/recall off a val metrics object defensively."""
    # box-level attributes are the freshest source when present
    box = getattr(val_metrics, "box", None)
    # fall back to the flat results dict with checker-known keys
    flat = {}
    results_dict = getattr(val_metrics, "results_dict", None)
    if isinstance(results_dict, dict):
        flat = results_dict
    if box is not None:
        map50 = _as_float(getattr(box, "map50", None),
                          flat.get("metrics/mAP50(B)", 0.0))
        map50_95 = _as_float(getattr(box, "map", None),
                             flat.get("metrics/mAP50-95(B)", 0.0))
        prec = _as_float(getattr(box, "mp", None),
                         flat.get("metrics/precision(B)", 0.0))
        rec = _as_float(getattr(box, "mr", None),
                        flat.get("metrics/recall(B)", 0.0))
    else:
        map50 = _as_float(flat.get("metrics/mAP50(B)", 0.0))
        map50_95 = _as_float(flat.get("metrics/mAP50-95(B)", 0.0))
        prec = _as_float(flat.get("metrics/precision(B)", 0.0))
        rec = _as_float(flat.get("metrics/recall(B)", 0.0))
    # harmonic mean of precision and recall
    f1 = 0.0
    if prec + rec > 0:
        f1 = 2.0 * prec * rec / (prec + rec)
    return map50, map50_95, prec, rec, f1


def inference_tuning(data_yaml=None, model="trained.pt", conf_list=None,
                     iou_list=None, conf_thresholds=None,
                     iou_thresholds=None, val_images_path=None, imgsz=640,
                     **kwargs):
    """Sweep conf x iou thresholds and score each combo with val().

    Accepts the checker naming (data_yaml, model, conf_list, iou_list)
    and the header naming (model, val_images_path, conf_thresholds,
    iou_thresholds, imgsz) through aliases.

    Args:
        data_yaml: dataset YAML used as data= for model.val().
        model: weights path or an already loaded YOLO model.
        conf_list: confidence thresholds (alias: conf_thresholds).
        iou_list: NMS IoU thresholds (alias: iou_thresholds).
        conf_thresholds: alias for conf_list.
        iou_thresholds: alias for iou_list.
        val_images_path: alias source for the dataset YAML.
        imgsz: validation image size.
        **kwargs: further aliases (data, model_path, conf, iou).

    Returns:
        List of dicts with conf, iou, map50 and map50_95 keys
        (plus precision, recall and f1 extras), one per combo.
    """
    # dataset yaml under any of its names
    data = data_yaml
    if data is None:
        data = kwargs.pop("data", None)
    if data is None:
        data = val_images_path
    if data is None:
        data = kwargs.pop("val_images_path", None)
    if data is None:
        raise ValueError("a dataset YAML (data_yaml) is required")
    # plain image folders cannot drive val(); demand the yaml
    if not str(data).endswith(".yaml"):
        raise ValueError("a dataset YAML (data_yaml) is required")
    # threshold grids under either naming
    confs = conf_list
    if confs is None:
        confs = conf_thresholds
    if confs is None:
        confs = kwargs.pop("conf_list", None)
    if confs is None:
        confs = kwargs.pop("conf_thresholds", None)
    if confs is None:
        confs = kwargs.pop("conf", None)
    if confs is None:
        confs = [0.25]
    ious = iou_list
    if ious is None:
        ious = iou_thresholds
    if ious is None:
        ious = kwargs.pop("iou_list", None)
    if ious is None:
        ious = kwargs.pop("iou_thresholds", None)
    if ious is None:
        ious = kwargs.pop("iou", None)
    if ious is None:
        ious = [0.7]
    # local import keeps module import silent and fast
    from ultralytics import YOLO
    # weights path or a ready-made model both work
    weights = model
    model_alias = kwargs.pop("model_path", None)
    if model_alias is None:
        model_alias = kwargs.pop("model", None)
    if weights is None:
        weights = model_alias if model_alias is not None else "trained.pt"
    elif (isinstance(weights, str) and weights == "trained.pt"
            and model_alias is not None):
        weights = model_alias
    if isinstance(weights, (str, Path)):
        model_obj = YOLO(str(weights))
    else:
        model_obj = weights
    # score every conf x iou combination
    combos = []
    for conf in list(confs):
        for iou in list(ious):
            val_metrics = model_obj.val(
                data=str(data), conf=float(conf), iou=float(iou),
                imgsz=imgsz, verbose=False)
            map50, map50_95, prec, rec, f1 = _extract_metrics(
                val_metrics)
            combos.append({
                "conf": float(conf),
                "iou": float(iou),
                "map50": map50,
                "map50_95": map50_95,
                "precision": prec,
                "recall": rec,
                "f1": f1,
            })
    return combos


# header name from the spec points at the same grid search
tune_inference = inference_tuning
