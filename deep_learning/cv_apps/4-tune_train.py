#!/usr/bin/env python3
"""Two-phase hyperparameter tuning and final YOLOv8 training."""

import shutil
from pathlib import Path

import yaml


# project paths; runs/ is cwd-relative, matching runs/detect/tune
BASE_DIR = Path(__file__).resolve().parent
DATA_YAML = str(BASE_DIR / "datasets" / "detection" / "data.yaml")
BASE_MODEL = "yolov8n.pt"
RUNS_DETECT = Path("runs") / "detect"
TUNE_GLOB = "tune*"
FINAL_NAME = "final"
BEST_MODEL_OUT = BASE_DIR / "best_model.pt"

# phase 1 search budget: short trials, enough to rank hyperparameters
TUNE_ITERATIONS = 18
TUNE_EPOCHS = 10
# phase 2 budget: continue from the tuned best to ~150 total epochs
FINAL_EPOCHS = 150
FINAL_PATIENCE = 25


def _yolo_cls():
    """Local import so module import stays silent and fast."""
    from ultralytics import YOLO
    return YOLO


def _tune_dir():
    """Return the latest tune run dir (tune, tune2, ...)."""
    # tune re-runs increment the folder name, so pick the newest
    cands = sorted(RUNS_DETECT.glob(TUNE_GLOB),
                   key=lambda p: p.stat().st_mtime)
    if cands:
        return cands[-1]
    return RUNS_DETECT / "tune"


def _best_hyperparams_path():
    """Return the tuned hyperparameters YAML path."""
    return _tune_dir() / "best_hyperparameters.yaml"


def _tune_best_weights():
    """Return the best weights path saved by the tune phase."""
    return _tune_dir() / "weights" / "best.pt"


def _load_best_hyperparams():
    """Load the tuned hyperparameters dict, or an empty dict."""
    path = _best_hyperparams_path()
    if not path.is_file():
        return {}
    with open(path) as f:
        params = yaml.safe_load(f) or {}
    # integer-only train args arrive as floats from the search
    try:
        from ultralytics.cfg import CFG_INT_KEYS
        int_keys = set(CFG_INT_KEYS)
    except ImportError:
        int_keys = {"close_mosaic", "patience", "workers", "seed"}
    clean = {}
    for key, value in params.items():
        if value is None:
            continue
        if key in int_keys and isinstance(value, float):
            value = int(round(value))
        clean[key] = value
    return clean


def run_tune_phase(data=DATA_YAML, weights=BASE_MODEL,
                   iterations=TUNE_ITERATIONS, epochs=TUNE_EPOCHS,
                   **overrides):
    """Run the lightweight model.tune() search and return its result."""
    # short trial trainings rank lr, augmentation and loss knobs
    # no project/name: tune defaults to runs/detect/tune by itself
    model = _yolo_cls()(weights)
    tune_kwargs = {
        "data": data,
        "epochs": epochs,
        "iterations": iterations,
    }
    tune_kwargs.update(overrides)
    return model.tune(**tune_kwargs)


def run_final_phase(data=DATA_YAML, weights=None, epochs=FINAL_EPOCHS,
                    patience=FINAL_PATIENCE, hyperparams=None,
                    **overrides):
    """Continue training from tuned weights and save best_model.pt."""
    # resume from the tuned best weights when no path is given
    if weights is None:
        weights = str(_tune_best_weights())
    # tuned hyperparameters become plain train() overrides
    params = dict(hyperparams) if hyperparams else {}
    params.update(_load_best_hyperparams())
    params.update(overrides)
    # continue to ~150 total epochs with early stopping
    # name only (no project): stable runs/detect/final folder
    model = _yolo_cls()(weights)
    train_kwargs = {
        "data": data,
        "epochs": epochs,
        "patience": patience,
        "name": FINAL_NAME,
        "exist_ok": True,
    }
    train_kwargs.update(params)
    model.train(**train_kwargs)
    # copy the final best weights next to this module
    final_best = RUNS_DETECT / FINAL_NAME / "weights" / "best.pt"
    shutil.copy(str(final_best), str(BEST_MODEL_OUT))
    return BEST_MODEL_OUT


def tune_hyperparameters():
    """Run tune search then final training; save best_model.pt."""
    # phase 1: genetic search over lr, augmentation and loss weights
    run_tune_phase()
    # phase 2: continue from best.pt with the winning hyperparameters
    run_final_phase()


if __name__ == "__main__":
    tune_hyperparameters()
