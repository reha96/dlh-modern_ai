# Resources — Computer Vision Architectures

Ingestion started 2026-08-24. Video transcripts pending; summaries below are
own words. Papers and docs summarized from knowledge of the canonical texts.

## Core CNN

### Watching

- **What is a convolution?** (3Blue1Brown)
  https://www.youtube.com/watch?v=KuXjwB4LzSA
  Date: 2026-08-24
  Visual walk-through of convolution as sliding a small kernel over a grid,
  multiplying and summing, in both 1-D signal and 2-D image settings. Builds
  the intuition that a convolution is a weighted local average whose weights
  are shared across every position.
- **CNNs**
  status: pending (URL to confirm on intranet)
  Date: 2026-08-24

### Reading

- **CS231n — Convolutional Neural Networks**
  https://cs231n.github.io/convolutional-networks/
  Date: 2026-08-24
  Stanford's reference chapter: layers as neurons, spatial arrangement
  hyperparameters (filter size, stride, padding), parameter counting formulas,
  pooling, and the conv → ReLU → pool pattern. The parameter-count table is
  the same math the checker's model summaries test.
- **Dive into Deep Learning — CNN Chapter**
  https://d2l.ai/chapter_convolutional-neural-networks/index.html
  Date: 2026-08-24
  From cross-correlation to full networks: channels, padding/stride effects
  on output shape, pooling mechanics, and LeNet as a worked example with code.
- **A Guide to Convolution Arithmetic for Deep Learning**
  https://arxiv.org/abs/1603.07285
  Date: 2026-08-24
  Pure geometry of convolution: exact output-size formulas for any
  kernel/stride/padding combination, illustrated step by step. Also covers
  transposed convolutions and their relation to gradient computation.
- **Understanding Convolutions — Distill**
  https://distill.pub/2021/understanding-convolutions/
  Date: 2026-08-24
  Interactive article deriving 2-D convolution from 1-D smoothing, then
  building to multi-channel inputs/outputs and why weight sharing makes
  translation equivariance natural.
- **Feature Visualization — Distill**
  https://distill.pub/2017/feature-visualization/
  Date: 2026-08-24
  Shows what individual filters learn via optimization: early layers detect
  edges/colors, deeper layers textures and object parts. Grounds the "feature
  hierarchy" objective of this project.

## Deep CNN

### Watching

- **Stanford CS231n Lecture 9 — CNN Architectures**
  https://www.youtube.com/watch?v=DAOcjicFr1Y
  Date: 2026-08-24
  Tour of landmark architectures (AlexNet → VGG → GoogLeNet → ResNet) with
  parameter/FLOP comparisons; explains why depth stalled until residual
  connections.
- **ResNet Explained**
  status: pending (URL to confirm on intranet)
  Date: 2026-08-24
- **Deep Residual Networks**
  status: pending (URL to confirm on intranet)
  Date: 2026-08-24
- **Depthwise Separable Convolutions**
  status: pending (URL to confirm on intranet)
  Date: 2026-08-24
- **MobileNets Architecture Explained**
  status: pending (URL to confirm on intranet)
  Date: 2026-08-24
- **EfficientNet Explained**
  status: pending (URL to confirm on intranet)
  Date: 2026-08-24

### Reading

- **Deep Residual Learning for Image Recognition** (He et al., 2015)
  https://arxiv.org/abs/1512.03385
  Date: 2026-08-24
  The ResNet paper. Degradation problem: plain deep nets underfit as depth
  grows; residual learning reformulates each block to fit F(x) + x so extra
  layers at worst act as identity. Defines basic and bottleneck blocks plus
  the 50/101/152 configurations this project rebuilds.
- **Xception: Deep Learning with Depthwise Separable Convolutions**
  (Chollet, 2016)
  https://arxiv.org/abs/1610.02357
  Date: 2026-08-24
  Argues Inception modules are an intermediate step between regular
  convolutions and depthwise separable convolutions; builds an architecture
  from pure depthwise separable layers and outperforms Inception V3.
- **MobileNetV2: Inverted Residuals and Linear Bottlenecks**
  (Sandler et al., 2018)
  https://arxiv.org/abs/1801.04381
  Date: 2026-08-24
  Expands channels first (inverted bottleneck), applies depthwise convolution
  in the expanded space, then projects back linearly; residual connections
  only between narrow layers. Justifies linear bottlenecks via information
  loss through ReLU on low-dimensional manifolds.
- **EfficientNet: Rethinking Model Scaling for CNNs** (Tan & Le, 2019)
  https://arxiv.org/abs/1905.11946
  Date: 2026-08-24
  Compound scaling: depth, width, and resolution should grow together under a
  fixed ratio instead of one at a time. Baseline EfficientNet-B0 found via
  neural architecture search.
- **DenseNet: Densely Connected Convolutional Networks**
  (Huang et al., 2016)
  https://arxiv.org/abs/1608.06993
  Date: 2026-08-24
  Concatenates each layer's output with all previous feature maps inside a
  dense block, strengthening gradient flow and feature reuse with few
  parameters; transition layers compress between blocks.
- **ResNeXt: Aggregated Residual Transformations** (Xie et al., 2016)
  https://arxiv.org/abs/1611.05431
  Date: 2026-08-24
  Adds a cardinality dimension (number of parallel grouped transforms) to
  residual blocks; matching accuracy with fewer parameters than widening.
