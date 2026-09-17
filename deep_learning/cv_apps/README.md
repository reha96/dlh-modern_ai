# Computer Vision Applications

YOLOv8 detection on a Pascal VOC 2012 subset (person/car/bicycle):
prepare the data, augment it with Albumentations, train, tune
hyperparameters, then tune inference thresholds.

## Layout

- `0-prep_data.py` — download VOC 2012, keep sampled images, convert
  XML boxes to YOLO labels, write `datasets/detection/` + `data.yaml`.
- `1-basic_aug.py` — `basic_aug(image, bboxes, labels)`: flip,
  brightness/contrast, affine jitter (seed 42).
- `2-custom_aug.py` — `custom_aug(image, bboxes, labels)`: motion blur
  plus one elastic/optical distortion (seed 42).
- `3-train_aug.py` — `train_with_augmentation(...)`: train YOLO with a
  custom Albumentations list, then `model.val()`; returns
  `(model, metrics)` with `.results_dict`.
- `4-tune_train.py` — `tune_hyperparameters()`: `model.tune()` search,
  then continue from `runs/detect/tune/weights/best.pt` to ~150 epochs;
  saves `best_model.pt` here.
- `5-tune_inference.py` — `inference_tuning(...)` (alias
  `tune_inference`): conf x iou grid search via `model.val()`, returns
  a list of `{conf, iou, map50, map50_95, ...}` dicts.
- `RESOURCES.md` — ingested intranet resources (done, do not touch).
- `datasets/`, `runs/`, `*.pt`, `*.tar` — generated, never committed.

## How to run

```bash
python3 0-prep_data.py        # needs train_samples.txt + val_samples.txt
python3 3-train_aug.py        # import train_with_augmentation instead
python3 4-tune_train.py       # GPU job: tune (~15-20 x ~10 epochs) + final
```

`0-prep_data.py` looks for `train_samples.txt` / `val_samples.txt` in
the current directory and in `cv_apps/` (the spec names the train file
twice; it means train + val). Without them it falls back to the full
VOC `ImageSets/Main/train.txt` / `val.txt` lists. The real VOC tarball
is ~2 GB; the full tune + 150-epoch train needs a GPU (Colab).

## Environment pins (checker: Ubuntu 20.04, Python 3.11)

- numpy 2.0.2, matplotlib 3.10.0, opencv 4.12.0.88
- torch 2.8.0, albumentations 2.0.8, ultralytics 8.4.7
- Code: `model.train / model.val / model.tune` (Ultralytics YOLOv8 API).
