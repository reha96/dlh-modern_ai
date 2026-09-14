# Computer Vision Applications — RESOURCES.md

Project: https://intranet-dlh.hbtn.io/projects/3715 (DLH campus).
Ingested 2026-09-14. Summaries are paraphrased; no verbatim text longer
than one sentence. Raw pages were not committed.

Section mapping: the intranet lists everything under one "Resources"
heading split into Object Detection (Foundations / Practical) and
Segmentation (Foundations / Practical). All items below got full
treatment except the dataset link (intranet-hosted file) and the
"explain to anyone" link (study-technique page, link only).

## Object Detection Foundations

## What is Object Detection? (Ultralytics Glossary)

URL: https://www.ultralytics.com/glossary/object-detection  ·  Date: unknown  ·  Status: summary

Detection means answering "what is where": each object gets a class
label, a bounding box, and a confidence score. Modern detectors are CNN
based, trained on sets like COCO, and cleaned up with non-max
suppression; box quality is scored with IoU.

- Detection = classification + localization (box + confidence).
- Key pipeline pieces: CNN features, NMS dedup, IoU evaluation.
- Detection vs classification ("what" vs "what is where"), vs instance
  segmentation (boxes vs pixel masks), vs tracking (single frame vs video).
- Typical uses: autonomous driving perception, retail checkout/shelves.
- Checker vocabulary: bounding box, confidence, NMS, IoU.

## R-CNN, Fast R-CNN, Faster R-CNN Explained (Lilian Weng)

URL: https://lilianweng.github.io/posts/2017-12-31-object-recognition-part-3/  ·  Date: 2017-12-31 (publication)  ·  Status: summary

The classic two-stage lineage: R-CNN classifies ~2k selective-search
proposals one by one, Fast R-CNN shares one CNN pass with RoI pooling
and a joint classification + box loss, Faster R-CNN folds proposal
generation into the network (RPN with anchors), and Mask R-CNN adds a
parallel mask branch with RoIAlign.

- Two-stage pattern: propose regions, then classify + refine boxes.
- Anchors: k boxes per sliding-window position (scales x ratios, e.g. 9).
- Bbox regression learns center shifts plus log scale/width-height tweaks.
- NMS + hard-negative mining are the standard cleanup tricks.
- Mask R-CNN = Faster R-CNN + mask branch; RoIAlign fixes quantization
  misalignment via bilinear interpolation.

## YOLO: You Only Look Once Explained (DataCamp)

URL: https://www.datacamp.com/blog/yolo-object-detection-explained  ·  Date: 2022-09-28 (publication)  ·  Status: summary

YOLO reframes detection as one regression pass: split the image into a
grid, have each cell predict boxes plus class probabilities, filter with
IoU and NMS. Its selling points are speed (tens of FPS), few background
errors, and open-source iteration from v1 through v10/v11/v12 and YOLO26.

- Single-shot = one forward pass, no separate proposal stage.
- Per-cell output vector: objectness pc, box coords, class scores.
- IoU drops weak grid candidates; NMS keeps the best box per object.
- v2 added anchors, batch norm, higher resolution; v3 multi-scale
  prediction; later versions decoupled heads, anchor-free designs,
  NMS-free training (v10).
- v1 limits: one object per cell hurts crowded/small-object scenes.

## Object Detection & Instance Segmentation Overview (COEP DSAI)

URL: https://coepdsai.github.io/2020/04/06/object-detection-and-instance-segmentation-overview.html  ·  Date: 2020-04-06 (publication)  ·  Status: summary

A compact tour from task definitions (detection, semantic, instance,
panoptic) through core concepts (boxes, anchors, IoU, NMS, binary masks,
mAP) to the R-CNN family and Mask R-CNN with its RoIAlign fix.

- Detection = localization (tight box) + classification.
- Anchor boxes tile the image; the net predicts offsets per anchor.
- IoU >= ~0.5 counts as a good prediction; NMS keeps the max-IoU box.
- Mask R-CNN adds a parallel mask head to Faster R-CNN for instance masks.
- mAP = mean of per-class average precision over IoU thresholds.

## Intersection over Union (IoU) for Detection & Segmentation (LearnOpenCV)

URL: https://learnopencv.com/intersection-over-union-iou-in-object-detection-and-segmentation/  ·  Date: 2022-06-28 (publication)  ·  Status: summary

IoU is overlap area divided by union area, in [0, 1]. In detection it is
a helper metric: with a threshold (often 0.5) it decides true vs false
positives, feeding precision/recall and mAP. In segmentation it is the
primary pixel-level score, computed from TP/FP/FN pixel areas.

- Formula: IoU = intersection / union; penalizes missed GT and overspill.
- Box IoU from corner coordinates; mask IoU from pixel AND/OR logic.
- Threshold choice flips TP/FP labels (0.5 loose, 0.75 strict).
- Implementations: NumPy by hand or torchvision `ops.box_iou`.
- mAP@0.5 / @0.75 are mAP values evaluated at those IoU thresholds.

## Non-Max Suppression Explained Visually (LearnOpenCV)

URL: https://learnopencv.com/non-maximum-suppression-theory-and-implementation-in-pytorch/  ·  Date: 2021-06-02 (publication)  ·  Status: summary

Detectors emit thousands of overlapping boxes from windowed/anchor
proposals, so NMS greedily keeps the highest-confidence box and deletes
neighbors whose IoU with it exceeds a threshold (commonly 0.5), repeating
until none remain. The single threshold drives the precision/recall
tradeoff of the cleanup.

- Input: boxes + scores + IoU threshold; output: kept boxes.
- Loop: pick max score, suppress high-IoU neighbors, repeat per class.
- High threshold keeps more boxes (recall up, duplicates up); low
  threshold is aggressive (precision up, misses up).
- Soft-NMS is the gentler follow-up worth knowing by name.

## Anchor Boxes Explained Intuitively (Ultralytics Glossary)

URL: https://www.ultralytics.com/glossary/anchor-boxes  ·  Date: unknown  ·  Status: summary

Anchors are fixed template rectangles (scale x aspect ratio) tiled over
each grid cell so the network predicts adjustments to a template instead
of raw coordinates. They are matched to ground truth by IoU during
training; classic detectors (Faster R-CNN, early YOLO) use them, while
newer YOLO versions are anchor-free.

- Anchors turn localization into offset regression + classification.
- One cell can hold several shapes (e.g. tall pedestrian + wide car).
- Sizes usually come from k-means clustering on the training set.
- Costs: tens of thousands of mostly-background anchors (focal loss
  helps) plus a final NMS pass.

## Mean Average Precision (mAP) Explained Clearly (Towards AI)

URL: https://towardsai.com/p/machine-learning/map-in-object-detection-i-bet-youll-remember-this-forever  ·  Date: 2025-09-28 (publication)  ·  Status: summary

The full metric chain worked example: sort detections by confidence,
label TP/FP at an IoU threshold, accumulate precision and recall, take
the area under the PR curve as AP (11-point interpolation), average over
classes for mAP, and average over IoU 0.5:0.95 for the COCO-style score.

- Precision = TP/(TP+FP); Recall = TP/(TP+FN = all ground truths).
- AP = area under the precision-recall curve, per class.
- mAP = mean AP over classes; mAP@0.5:0.95 averages ten IoU thresholds.
- Confidence threshold moves along the PR curve (precision vs recall).
- Task 4 targets (mAP50 >= 65%, mAP50-95 >= 46%) sit on this scale.

## Practical Understanding (Detection)

## Data Augmentation using Ultralytics YOLO

URL: https://docs.ultralytics.com/guides/yolo-data-augmentation  ·  Date: ~2026-09-08 (page footer "Updated 6 days ago" on 2026-09-14)  ·  Status: summary

The reference for every built-in YOLO augmentation knob with ranges and
defaults: HSV color jitter, geometric transforms (degrees, translate,
scale, shear, perspective, flips), multi-image mixes (mosaic, mixup,
cutmix, copy-paste), plus custom Albumentations lists passed as
`augmentations=` which replace the tiny default Albumentations set.

- HSV defaults: hsv_h=0.015, hsv_s=0.7, hsv_v=0.4; flip left-right 0.5.
- Mosaic default 1.0; `close_mosaic` switches mosaic/mixup/cutmix/
  copy-paste off for the final epochs.
- Custom Albumentations transforms move boxes/polygons/masks with the
  image; keep the list small to protect epoch time.
- Start simple and mirror production conditions; color jitter first,
  geometry only if the camera viewpoint varies.

## Advanced Image Augmentation with Albumentations

URL: https://www.geeksforgeeks.org/nlp/enhancing-deep-learning-models-with-albumentations-a-guide-to-image-augmentation/  ·  Date: 2024-07-19 (publication)  ·  Status: summary

A hands-on intro to the Albumentations library: pip-installable,
pipeline-friendly, 60+ transforms (geometric, color, noise, weather such
as rain/snow/fog/sun-flare/shadow), and designed to carry bounding boxes,
masks, and keypoints along with the image.

- `A.Compose([...])` pipelines; per-transform `p` controls probability.
- One call handles image + bboxes + labels jointly (Tasks 1-2 pattern).
- Weather/lighting effects simulate deployment conditions cheaply.
- Relevant to Task 2's motion blur / elastic / optical-distortion picks.

## Train with YOLO (Ultralytics)

URL: https://docs.ultralytics.com/modes/train  ·  Date: ~2026-09-11 (page footer "Updated 3 days ago" on 2026-09-14)  ·  Status: summary

The training manual: `YOLO("yolov8n.pt").train(data=..., epochs=...,
imgsz=..., batch=...)`, device selection (cuda/cpu/mps), resume from
checkpoints, early stopping via patience, and the full hyperparameter
table (lr0, momentum, weight decay, warmup, loss weights box/cls/dfl,
optimizer choices incl. auto -> AdamW/MuSGD).

- Transfer learning: start from pretrained .pt, fine-tune on custom YAML.
- `data.yaml` carries train/val paths, class count, and names.
- `patience` stops training when validation fitness plateaus.
- `batch=-1` auto-sizes to GPU memory; OOM auto-retries by halving.
- Task 3's wrapper maps onto these exact arguments.

## Predict / Inference with YOLO

URL: https://docs.ultralytics.com/modes/predict  ·  Date: ~2026-09-10 (page footer "Updated 4 days ago" on 2026-09-14)  ·  Status: summary

The inference manual: `model.predict(source, conf=0.25, iou=0.7,
imgsz=640, ...)` over images, videos, streams, and directories, with
`stream=True` for memory-efficient generators and Results objects
exposing boxes, masks, confidences, and class names.

- `conf` gates detections (fewer false positives when raised); `iou`
  drives NMS dedup (lower = fewer boxes).
- Task 5's grid search sweeps exactly these two knobs via `model.val()`.
- `max_det` caps boxes per image; `classes=` filters to wanted IDs.
- `save_txt`/`save_crop` export labels and crops for analysis.

## Hyperparameter Tuning with YOLO

URL: https://docs.ultralytics.com/guides/hyperparameter-tuning  ·  Date: ~2026-09-07 (page footer "Updated 1 week ago" on 2026-09-14)  ·  Status: summary

`model.tune()` runs a genetic search: fitness-weighted parent selection,
range-normalized Gaussian mutation of ~half the parameters per
iteration, short trial trainings, results in NDJSON plus
`runs/detect/tune/best_hyperparameters.yaml` and `weights/best.pt`
for the winning iteration.

- `iterations` = number of sequential trial trainings (default 300).
- Search space spans lr0/lrf, momentum, weight decay, warmup, loss
  weights, and augmentation strengths.
- Resume with `resume=True` plus the original arguments.
- Task 4's two-phase plan (short tune, then continue from best.pt to
  ~150 epochs) follows this guide directly.

## Object Detection Model Optimization Techniques

URL: https://medium.com/academy-team/model-optimization-techniques-for-yolo-models-f440afa93adb  ·  Date: 2025-07-03 (publication)  ·  Status: summary

A survey of the speed-vs-accuracy tradeoff levers: picking the model
scale (n/s/m/l/x), input resolution (320 vs 640), FP16 half precision,
hyperparameter tuning, TensorRT (layer fusion, INT8), architecture edits
(pruning, quantization, lighter backbones, distillation), and data
augmentation such as mosaic (+2-3% mAP claimed).

- Real-time bar: ~30+ FPS; smaller imgsz trades mAP for FPS.
- FP16/TensorRT/INT8 buy large speedups for small mAP costs.
- Batch/workers/epochs/patience/lr/momentum/weight-decay starter ranges
  mirror the Ultralytics tables.
- Useful framing for Task 4/5 tuning choices, not a how-to.

## Segmentation Foundations

## Instance Segmentation Explained

URL: https://blog.roboflow.com/instance-segmentation/  ·  Date: 2026-03-25 (publication)  ·  Status: summary

Instance segmentation outputs a pixel mask per object instance plus
label and score, unlike boxes (detection) or class-only pixel maps
(semantic). The guide walks the full loop: polygon/SAM-assisted labeling
in Roboflow Annotate, training (RF-DETR-Seg / YOLO-seg / Detectron2),
COCO-format polygon storage, and deployment in Workflows.

- Mask = exact pixels of one object; separates overlapping same-class
  instances that boxes and semantic maps merge.
- Costs: heavier annotation (polygons), bigger models, slower inference.
- COCO stores segments as x,y polygon point lists plus bbox and area.
- Use when shape, boundaries, overlap, or area measurement matter.

## Semantic vs Instance Segmentation

URL: https://www.v7darwin.com/blog/semantic-segmentation-guide  ·  Date: 2021-09-16 (publication)  ·  Status: summary

Semantic segmentation labels every pixel by class (all cars = one "car"
region) using encoder-decoder nets (FCN, U-Net with skip connections,
PSPNet pyramid pooling, DeepLab atrous convolutions); instance
segmentation additionally splits same-class pixels into separate
objects. Loss functions covered: pixel-wise cross-entropy, focal loss
for class imbalance, Dice loss for overlap.

- Semantic: "what class is each pixel"; instance: "which object".
- U-Net skips rescue spatial detail lost in downsampling.
- Focal loss down-weights easy pixels; Dice scores mask overlap.
- Crowded same-class scenes are where semantic maps fail and instance
  masks win.

## What Is Instance Segmentation? (IBM)

URL: https://www.ibm.com/think/topics/instance-segmentation  ·  Date: unknown  ·  Status: summary

IBM's primer contrasts instance vs semantic vs panoptic segmentation
(countable "things" vs uncountable "stuff") and explains the model
zoo: two-stage Mask R-CNN (detect then segment, accurate but slower)
vs one-shot YOLACT-style models (parallel branches, faster), plus
transformer/Swin variants. Training notes stress costly hand annotation
and standard sets (COCO, ADE20K, Cityscapes).

- Instance = detect + pixel mask per thing; panoptic adds stuff labels.
- Mask R-CNN = Faster R-CNN + FCN mask head; one-shot trades accuracy
  for real-time speed.
- Evaluation: mask IoU plus AP/mAP, often at IoU thresholds (AP50).
- IoU limits: blind to near-vs-far misses, non-differentiable (GIoU fix).

## What Is a Segmentation Mask?

URL: https://www.v7darwin.com/blog/image-segmentation-guide  ·  Date: 2021-08-12 (publication)  ·  Status: summary

Masks in context: segmentation groups pixels under class labels via an
encoder-decoder net, with annotation ranging from polygons to
box-prompted auto-annotation. Covers the three task types, classical
methods (thresholding, region growing, edges, k-means clustering), deep
models (SegNet, U-Net, DeepLab), and applications from medical imaging
to driving and aerial surveys.

- Binary/n-channel masks: per-class channels of 0/1 over the image.
- Polygon waypoints trade precision for speed; auto-annotate refines a
  box prompt into a boundary.
- Instance/panoptic annotation must handle overlaps, unlike semantic.
- Classical methods are fast but brittle on complex scenes.

## Polygon Annotation vs Bounding Boxes (Roboflow)

URL: https://docs.roboflow.com/datasets/annotate/annotate/use-roboflow-annotate  ·  Date: unknown (docs site, no Last-Modified header)  ·  Status: summary

Roboflow Annotate's toolset: drag-select editing, box tool (click-drag +
class), polygon tool (vertex clicks, close on first vertex), brush tool
for pixel masks, Smart Polygon (SAM-powered click-to-mask with
add/remove), Label Assist (model-suggested boxes), plus convert actions
(box <-> polygon <-> mask) and merge-masks union.

- Boxes: fast, enough for detection; polygons/masks: required for
  segmentation training.
- Smart Polygon and brush capture irregular shapes (hair, foliage,
  transparency) far faster than manual vertices.
- Convert/merge actions let one annotation serve both Task 0-style box
  labels and segmentation masks.

## Mask IoU vs Box IoU Explained

URL: https://encord.com/blog/image-segmentation-for-computer-vision-best-practice-guide/  ·  Date: 2024-12-04 (publication)  ·  Status: summary

Encord's best-practice guide spans segmentation types, classical vs deep
techniques (U-Net, SegNet, DeepLab, SAM), metrics, and datasets
(Berkeley, Pascal VOC, COCO). For the IoU question: box IoU uses
rectangle overlap while mask IoU counts pixel-level
intersection/union; sibling metrics are pixel accuracy (blind to
imbalance and alignment), Dice/F1-style overlap (imbalance-robust), and
Jaccard/IoU (also alignment-aware).

- Mask IoU = AND pixels / OR pixels; box IoU = rectangle areas.
- Dice = 2*intersection / (sum of areas); monotonically related to IoU.
- Pascal VOC (20 classes, pixel labels) is this project's Task 0 source.
- SAM enables prompt-based auto-segmentation, cutting annotation cost.

## Bounding Box mAP vs Segmentation mAP

URL: https://softwaremill.com/instance-segmentation-evaluation-criteria/  ·  Date: 2022-08-16 (publication)  ·  Status: summary

The computation is identical (PR curve area per class, averaged); only
the IoU underneath changes: box overlap for detection mAP, mask overlap
for segmentation mAP. Also notes IoU's blind spots (zero whether near or
far, non-differentiable, so GIoU for losses) and the COCO convention of
averaging AP over IoU 0.5:0.95.

- Same mAP machinery, different matching criterion (boxes vs masks).
- Duplicate detections of one GT: first is TP, rest FP.
- 11-point interpolation smooths the zigzag PR curve into one number.
- Segmentation mAP is stricter: sloppy boundaries fail at high IoU.

## Practical Understanding (Segmentation)

## How NMS Works in Instance Segmentation (Mask R-CNN context)

URL: https://arxiv.org/abs/1703.06870  ·  Date: 2017-03-20 (publication)  ·  Status: summary

The Mask R-CNN paper (He et al.): Faster R-CNN plus a parallel FCN mask
branch per RoI, trained with L = Lcls + Lbox + Lmask (binary
cross-entropy per class, no cross-class competition). RoIAlign replaces
quantizing RoIPool with bilinear sampling for pixel-accurate features.
NMS itself still runs on boxes/scores before masks are emitted, so
overlapping instances survive only if their boxes differ enough; the
masks then disambiguate the shared pixels.

- Mask branch outputs K binary m x m masks, one per class.
- Decoupled design: classify once, segment with the matching class mask.
- RoIAlign matters most for small/overlapping objects.
- Top COCO results on all three tracks at publication (5 fps).

## Object Detection vs Image Segmentation

URL: https://www.ultralytics.com/blog/what-is-mask-r-cnn-and-how-does-it-work  ·  Date: 2025-03-21 (publication)  ·  Status: summary

Uses Mask R-CNN's story to draw the detection/segmentation line: boxes
are cheap rectangles that include background and merge overlaps, while
masks trace exact contours. Walks the architecture (ResNet+FPN backbone,
RPN anchors, RoIAlign, parallel classify/refine/mask heads), admits the
costs (GPU-hungry, slower, data-hungry, fiddly), and points at one-stage
models (YOLO11: 22% fewer params than v8m at higher COCO mAP) for
real-time work.

- Detection answers "what is where" coarsely; segmentation answers it
  per pixel (learning objective 8 vs 16 in the spec).
- Mask R-CNN ~2017 FAIR milestone; industry now favors single-pass YOLO.
- When to segment: occlusion, shape, measurement; when to detect:
  counting, tracking, speed.

## Study Technique + Dataset

## Feynman Learning Technique ("explain to anyone")

URL: https://fs.blog/feynman-learning-technique/  ·  Status: link only

The intranet's "explain to anyone" learning-objectives link. Included
for completeness; it is a study method, not a CV reference.

## segmentation_set.zip (intranet dataset)

URL: intranet-hosted (see project page Dataset section)  ·  Status: deferred

Auth-gated download for the segmentation tasks; organize unzipped
contents under `datasets/segmentation/`. Inspect shapes/keys locally
after download; no summary applicable.

## Quiz Hooks

- IoU — overlap/union in [0,1]; threshold turns detections into TP/FP.
- NMS — keep max-confidence box, suppress high-IoU neighbors, repeat.
- Anchor box — fixed template rectangle the net regresses offsets from.
- Single-shot detector — one forward pass, no proposal stage (YOLO).
- mAP — mean over classes of PR-curve area; @0.5 loose, @0.5:0.95 strict.
- Precision vs recall — accuracy of positives vs fraction of GT found.
- Semantic vs instance — per-pixel class vs per-object masks.
- Segmentation mask — binary/n-channel pixel map of object shape.
- Polygon annotation — vertex list tracing an object boundary for masks.
- Mask IoU — pixel AND/OR instead of rectangle overlap.
- RoIAlign — bilinear-sampled region features, no quantization shift.
- Mosaic — 4-image composite augmentation; close it before training ends.
- `model.tune()` — genetic hyperparameter search saving best.yaml + best.pt.
- conf vs iou at inference — detection gate vs NMS dedup strictness.
