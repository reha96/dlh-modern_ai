# Transfer Learning for Computer Vision — Resources

Project: Transfer Learning for Computer Vision (intranet 3655) · Dir: `deep_learning/transfer_learning`
Ingested: 2026-09-17 · Session alive for project pages (direct /projects/3655 loads; /projects/current redirects to /auth/login, so health check is unreliable — rltokens resolved in-context via request API, 18/18).
Sections on project page: Watch (5 YouTube) · Read (12) · Definitions to skim (none — section absent) · References (none — section absent).
Label-mismatch warning: 2 Watch links and 2 Read links resolve to content unrelated to their intranet labels (details inline). Summaries below describe the actual destinations.

## Python: Lambda, Map, Filter, Reduce Functions (intranet label: "Transfer learning overview — Stanford CS231n Lecture 13")

URL: https://www.youtube.com/watch?v=cKlnR-CB3tk  ·  Date: 2016-06-07 (YouTube upload)  ·  Status: summary (label mismatch: video is a Python basics tutorial, not CS231n)

A short Python programming tutorial with no transfer-learning content: it defines one-line lambda functions, then shows map for applying a function to every list item, filter for keeping items that pass a test, and reduce for collapsing a list to one value. The pedagogy is "write the plain loop first, then the one-liner", aimed at beginners meeting functional-style helpers.

- Intranet label does not match the destination; do not cite this as a transfer-learning source.
- Lambda = anonymous one-line function; map/filter return transformed or selected items; reduce folds a list into a single result.
- Only incidental value here: Python fluency used in every task file.
- Transcript (227 segments, ~1.8k words) kept outside the repo in /tmp/opencode/tl3655/.

## Variational Autoencoders — Arxiv Insights (intranet label: "Transfer learning explained — DeepLearningAI")

URL: https://www.youtube.com/watch?v=9zKuYvjFFS8  ·  Date: 2018-02-25 (YouTube upload)  ·  Status: summary (label mismatch: video covers VAEs, not transfer learning)

A technical walkthrough of autoencoders that compress high-dimensional input into a smaller latent space and rebuild it, then extends the idea to variational autoencoders, which learn a distribution over the latent space instead of fixed points so new samples can be generated. It assumes comfort with backpropagation and spends most time on the probabilistic framing behind VAEs.

- Intranet label does not match the destination; useful for generative-model background, not for this project's tasks.
- Core contrast: plain autoencoder reconstructs inputs, variational autoencoder models a latent distribution for sampling.
- Latent-space compression intuition transfers loosely to why frozen CNN features are reusable.
- Transcript (441 segments, ~3.0k words) kept outside the repo in /tmp/opencode/tl3655/.

## Using Pretrained Neural Networks with Keras (6.3) — Jeff Heaton

URL: https://www.youtube.com/watch?v=TXqI9fp0imI  ·  Date: 2021-12-08 (YouTube upload)  ·  Status: summary

A course segment arguing that practitioners should start from state-of-the-art pretrained networks rather than guessing filter counts, depths, and widths from scratch. It demonstrates loading a pretrained model in a notebook, using it directly for prediction, and retraining it on new data, framing transfer learning as a way to skip most of the training cost and architecture guesswork.

- Pretrained nets answer "how many layers/filters?" by reusing architectures proven on ImageNet.
- Two uses shown: inference out of the box and retraining the network for a new task.
- Matches task 0/1 thinking: load with ImageNet weights, attach a new head.
- Transcript (202 segments, ~1.2k words) kept outside the repo in /tmp/opencode/tl3655/.

## The Ultimate Guide to Fine-Tuning Pre-Trained Models in TensorFlow & Keras — OpenCV University

URL: https://www.youtube.com/watch?v=10uDPsdAUdY  ·  Date: 2023-04-18 (YouTube upload)  ·  Status: summary

A long-form guide contrasting out-of-the-box pretrained inference with repurposing a backbone for custom data, centered on fine-tuning as the most flexible option. It works through a VGG16 classification example on a traffic-sign dataset, covering when frozen features suffice, how unfreezing with a small learning rate adapts representations, and why pretrained weights matter most when data or compute is limited.

- Decision ladder: broad ImageNet-like classes work out of the box; custom narrow tasks need a new head; stubborn gaps need fine-tuning.
- Fine-tuning recipe preview: train head first, then unfreeze top backbone layers at a low learning rate.
- Directly supports tasks 1, 2, and 4 (head training, unfreezing, full pipeline).
- Transcript (919 segments, ~6.3k words) kept outside the repo in /tmp/opencode/tl3655/.

## Regularization — Data Augmentation and Transfer Learning — Alexander Jung

URL: https://www.youtube.com/watch?v=8-bLOSTBgG8  ·  Date: 2021-11-08 (YouTube upload)  ·  Status: summary

A university lecture framing nearly all of deep learning practice as regularization, then developing two popular techniques in depth: data augmentation (artificially expanding the training set with realistic transformations) and transfer learning (reusing features learned on a large source task). The through-line is that both methods constrain the model toward solutions that generalize instead of memorizing a small dataset.

- Transfer learning and augmentation presented as sibling regularizers against overfitting.
- Augmentation exposes the model to variants of the data it would otherwise never see.
- Early-layer reuse rationale: generic features transfer, task-specific top layers do not.
- Directly supports tasks 3 and 4 (augmentation pipeline, small-data Caltech-101 training).
- Transcript (993 segments, ~5.6k words) kept outside the repo in /tmp/opencode/tl3655/.

## Transfer learning notes — CS231n

URL: https://cs231n.github.io/transfer-learning/  ·  Date: unknown (course notes carry no byline date)  ·  Status: summary

The canonical short reference for this project: because few teams have ImageNet-scale data, the standard move is pretraining on a huge dataset and reusing the network as initialization or as a fixed feature extractor (CNN codes off the penultimate layer, trained into a linear classifier). It gives the four-case rule of thumb keyed on dataset size versus similarity to the source data, plus the practical warnings to use smaller learning rates on fine-tuned weights and to keep images' preprocessing consistent with pretraining.

- Four cases: small+similar trains a linear head on CNN codes; large+similar fine-tunes everything; small+different trains the head on earlier-layer activations; large+different still benefits from pretrained initialization.
- Early layers hold generic detectors (edges, blobs); late layers hold source-task specifics (e.g. dog-breed features).
- Fine-tuned weights get a smaller learning rate than the randomly initialized head.
- Feature-extraction workflow (task 0/1) versus fine-tuning workflow (task 2/4) comes straight from this page.

## Anti-Chaos Control paper (intranet label: "Comprehensive guide to transfer learning applications")

URL: https://arxiv.org/abs/1812.02818  ·  Date: 2018-11-19 (arXiv submission)  ·  Status: summary (label mismatch: link resolves to an optics/control paper, not a transfer-learning guide)

The arXiv identifier behind this rltoken points to a paper on nonlinear control for secure optical communication, which has no connection to transfer learning. No transfer-learning guidance can be drawn from the destination; the intranet label appears garbled.

- Do not cite this identifier for transfer-learning claims.
- If a "comprehensive applications guide" is needed, use the Keras transfer-learning guide and the PyTorch tutorial entries instead.

## Pretrained CNN models in Keras — Keras Applications

URL: https://keras.io/api/applications/  ·  Date: 2026-08-26 (page last modified)  ·  Status: summary

The reference catalog of Keras backbones with ImageNet weights, pairing each model with size, accuracy, parameter count, depth, and CPU/GPU inference time. It documents the shared constructor pattern (weights, include_top, input_shape, pooling, classes), automatic weight downloads into ~/.keras/models/, and worked snippets for classifying, extracting features with include_top=False, pulling an intermediate layer's output, and the canonical two-stage fine-tune of InceptionV3.

- Constructor pattern behind task 0: weights="imagenet", include_top=False, input_shape=(224, 224, 3).
- Model-choice table (MobileNetV2: 14 MB, 71.3% top-1; ResNet50: 98 MB, 74.9%; EfficientNetB0: 29 MB, 77.1%) supports task 4 backbone selection.
- recompile-after-trainable-changes rule is stated explicitly here and in the guides.
- Fine-tune snippet freezes all layers, trains the head, then unfreezes from a cutoff layer at low learning rate — the task 2/4 template.

## ResNet architecture — Deep Residual Learning for Image Recognition (He et al.)

URL: https://arxiv.org/abs/1512.03385  ·  Date: 2015-12-10 (arXiv submission)  ·  Status: summary

The residual-learning paper: reformulating deep layers to fit residual functions of their inputs lets networks reach 152 layers with lower complexity than VGG while winning ILSVRC 2015 at 3.57% top-5 error. The key mechanism is the skip connection, which gives gradients a direct path and turns depth from an optimization liability into accuracy gains, with the same representations later lifting COCO detection substantially.

- Skip connections are why very deep backbones (ResNet50/101 in tasks 2/4) stay trainable.
- Depth-without-complexity argument justifies picking ResNet variants over VGG for fine-tuning.
- Empirical anchors: 152 layers at 8x VGG depth, 3.57% ImageNet test error, COCO improvement from depth alone.

## EfficientNet architecture and scaling (Tan & Le)

URL: https://arxiv.org/abs/1905.11946  ·  Date: 2019-05-28 (arXiv submission; revision 2020-09-11)  ·  Status: summary

The compound-scaling paper: instead of growing depth, width, or resolution alone, scaling all three together with one coefficient yields strictly better accuracy-per-parameter, and the NAS-designed EfficientNet family built on that rule beats older ConvNets while transferring strongly (notably on CIFAR-100). EfficientNet-B7 hit 84.3% ImageNet top-1 at a fraction of the size and inference cost of the prior best.

- Compound scaling (depth x width x resolution) is the vocabulary for comparing backbones in task 4.
- Efficiency angle matters for the checker-style environment: B0 reaches 77.1% top-1 at 5.3M params versus ResNet50's 25.6M.
- Transfer-strength claim supports choosing EfficientNet/MobileNet-family backbones for Caltech-101.

## Using pretrained models for transfer learning in Keras — Keras guide (fchollet)

URL: https://keras.io/guides/transfer_learning/  ·  Date: 2023-06-25 (last modified; created 2020-04-15)  ·  Status: summary

The single most task-relevant guide: it defines the freeze-head-train then unfreeze-at-low-LR two-phase workflow, explains the trainable flag and its recursive propagation, and warns that randomly initialized heads must converge before fine-tuning or their huge gradients destroy pretrained features. It adds the two BatchNormalization rules that most checkers fingerprint: call the base model with training=False so batch statistics never update, and always recompile after touching any trainable flag.

- Phase order (task 4): freeze base, train head to convergence, unfreeze top layers, retrain at ~1e-5.
- layer.trainable = False moves weights to non-trainable; compile() snapshots trainable state, so recompile after every change.
- BN layers carry non-trainable mean/variance statistics that get wrecked by training-mode updates during fine-tuning.
- Lightweight alternative noted: run the base once and train a small model on cached features (fast, but blocks augmentation).

## Transfer learning tutorial — PyTorch (Sasank Chilamkurthy; concepts apply to Keras)

URL: https://docs.pytorch.org/tutorials/beginner/transfer_learning_tutorial.html  ·  Date: 2025-01-27 (last updated; created 2017-03-24)  ·  Status: summary

The ants-versus-bees tutorial that demonstrates both canonical scenarios on ~120 images per class: fine-tuning all of ResNet18 with a replaced final layer and SGD with step decay, versus freezing everything but the new head. The frozen variant reaches comparable accuracy in about half the CPU time because gradients skip most of the network, and the tutorial pairs both with train-only augmentation (random resized crops, horizontal flips) plus ImageNet normalization on both splits.

- Small-data proof point: ~240 training images generalize via transfer where from-scratch training cannot.
- Freeze-all-but-head versus fine-tune-all is the same A/B the project runs across tasks 1, 2, and 4.
- Augmentation-on-train / normalize-everywhere split mirrors the task 3/4 pipeline.
- LR schedule (StepLR, gamma 0.1 every 7 epochs) and best-checkpoint saving are the callback patterns for task 4.

## Transfer learning example in Keras — GeeksforGeeks

URL: https://www.geeksforgeeks.org/deep-learning/transfer-learning-fine-tuning-using-keras/  ·  Date: 2025-07-23 (last updated)  ·  Status: summary

A worked VGG16-on-CIFAR-10 recipe in seven steps: normalize pixels, load the base without its top, append global pooling plus dense/softmax layers, freeze and train the head, then unfreeze the last layers and retrain at 1e-4 before plotting accuracy/loss curves. Its reported numbers are modest (low-60s validation accuracy), which usefully sets expectations for a heavy backbone on tiny 32x32 inputs without resizing or augmentation.

- Step order mirrors the project arc: head training (task 1), partial unfreezing (task 2), curves (task 4 callbacks/plots).
- Cautionary detail: feeding 32x32 images straight into an ImageNet backbone underperforms; the project mains resize to 224 first.
- Unfreeze-last-N-layers at Adam(1e-4) is the concrete fine-tuning hyperparameter starting point.

## Training & evaluation guide for fine-tuning in Keras

URL: https://keras.io/guides/training_with_built_in_methods/  ·  Date: 2023-06-25 (last modified; created 2019-03-01)  ·  Status: summary

The mechanics manual for compile/fit/evaluate/predict: how losses, optimizers, and metrics are wired at compile time, how validation_split carves a holdout from NumPy data (last fraction before shuffling, NumPy only), how tf.data and PyDataset objects plug into fit, and how EarlyStopping, ModelCheckpoint, and ReduceLROnPlateau callbacks automate the training loop. Its examples use MNIST MLPs, but every signature carries over to the transfer-learning mains.

- compile(optimizer, loss, metrics) then fit with validation_data or validation_split (task 1/2 mains).
- Callbacks bank for task 4: EarlyStopping on val_loss/val_accuracy, ModelCheckpoint save_best_only, ReduceLROnPlateau.
- validation_split takes the trailing fraction pre-shuffle and is unsupported for Dataset objects — shuffle explicitly in the tf.data pipeline instead.
- class_weight/sample_weight dicts are available if Caltech-101 imbalance bites.

## Fast scrambling paper (intranet label: "Progressive resizing & learning rate strategies")

URL: https://arxiv.org/abs/1805.08215  ·  Date: 2018-05-21 (arXiv submission; revised 2019-04-02)  ·  Status: summary (label mismatch: link resolves to a quantum-information paper, not a training-strategies guide)

The identifier behind this rltoken points to a paper on fast scrambling in sparse graphs, unrelated to progressive resizing or learning-rate schedules. No training-strategy content can be drawn from the destination; the intranet label appears garbled.

- Do not cite this identifier for LR-schedule or resizing claims.
- For the actual strategies, use the Keras guides (ReduceLROnPlateau, two-phase LR) and the PyTorch tutorial (StepLR) entries instead.

## Data augmentation for transfer learning — Perez et al.

URL: https://arxiv.org/abs/1712.04621  ·  Date: 2017-12-13 (arXiv submission)  ·  Status: summary

An empirical comparison of augmentation strategies under artificially constrained ImageNet subsets: classic geometric transforms (crop, rotate, flip) remain among the most successful approaches, GAN-synthesized styles are explored, and a learned "neural augmentation" policy is proposed with mixed results across datasets. The takeaway for small-data transfer is conservative: standard flips/crops/rotations reliably help, exotic synthesis is situational.

- Justifies the task 3 layer set: horizontal flip, rotation, zoom, contrast are the proven core.
- Small-subset methodology matches the project's CIFAR-10/Caltech-101 regime.
- Learned-augmentation caveat: keep the pipeline simple and seeded before trying anything exotic.

## Transfer learning: feature extraction and fine-tuning — Alessandro Bosco

URL: https://medium.com/data-reply-it-datatech/transfer-learning-feature-extraction-and-fine-tuning-db7d82767992  ·  Date: 2024-03-26 (publication; archived 2024-07-18)  ·  Status: summary (via archive.org; Medium paywall bypassed through public snapshot)

A compact article contrasting the two transfer techniques by how much of the pretrained network moves: feature extraction freezes the base and trains only a new classifier on its outputs (cheap, good for small or compute-limited tasks), while fine-tuning unfreezes top layers and jointly retrains them with the head at greater cost and overfitting risk. It repeats the layer-selection rule (higher-layer features when source and target are similar, lower-layer features when they differ) and names dropout plus early stopping as the standard guards.

- Freeze-rule of thumb: similar datasets reuse top features; different datasets drop to earlier, more general activations.
- Cost framing: extraction trains only the head; fine-tuning backprops through far more parameters.
- Overfitting guards named: dropout, early stopping — both appear in the reference-fork solutions.
- Retrieval note: fetched via the web.archive.org snapshot per the paywall chain; no login-wall content used.

## Quiz Hooks

- Feature extraction — freeze the pretrained base, train only a new classifier on its outputs.
- Fine-tuning — unfreeze top backbone layers and retrain them with the head at a very low learning rate.
- CNN codes — feature vectors from the layer before the original classifier, used to train a linear head.
- trainable flag — setting it False moves weights to non-trainable; recompile after any change or it is ignored.
- BatchNormalization trap — keep the base call at training=False during fine-tuning or batch statistics get destroyed.
- CS231n four cases — dataset size crossed with source similarity decides head-only versus full fine-tune.
- Compound scaling — EfficientNet scales depth, width, and resolution together for accuracy per parameter.
- Residual connection — skip connections let gradients flow through 100+ layer backbones.
- Data augmentation — train-time random flips/rotations/zooms that regularize small-data transfer.
- GlobalAveragePooling2D — parameter-free spatial collapse from (7, 7, 1280) to a 1280-vector.
- include_top=False — drops the 1000-class ImageNet head so a custom classifier can be attached.
- Validation split — trailing fraction of NumPy data, taken before shuffling; unavailable for Dataset objects.
