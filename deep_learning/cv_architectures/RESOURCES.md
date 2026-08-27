# Resources — Computer Vision Architectures

Ingestion started 2026-08-24. Updated 2026-08-27. Summaries below are
own words, no verbatim longer than one sentence. Papers and docs
summarized from the canonical texts; transcripts summarized from
auto-captions.

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

## Potential New Sources

- **CNN Explainer — Learning Convolutional Neural Networks with Interactive Visualization**
  https://poloclub.github.io/cnn-explainer/
  Paper: https://arxiv.org/abs/2004.15004 — Wang, Turko, Shaikh, Park, Das, Hohman, Kahng, Chau, IEEE TVCG 2020.
  Date: 2026-08-27
  Teaching tool built at Georgia Tech / Oregon State for non-experts.
  Runs in the browser with TensorFlow.js, no install. Uses a small
  Tiny-VGG-like model trained on a subset with 10 output classes so
  everything can run live. What it shows: a top overview of the model
  graph with shape annotations, then click any layer to drill into the
  low-level math — convolution as sliding dot products, activation
  heatmaps, pooling downsampling, flatten and fully-connected scoring.
  Hover ties activations back to the input pixels, and the detailed
  formula view sits next to the interactive heatmap so you see the same
  numbers both ways. Smooth animation carries you between overview and
  detail, which is the paper's main design claim. Prior work identified
  novice pain points via instructor interviews and a student survey; a
  small qualitative study reported better grasp and higher engagement.
  Code and training scripts under `tiny-vgg/` on GitHub (MIT).
- **3D Visualization of a Convolutional Neural Network — Adam Harley**
  https://adamharley.com/nn_vis/cnn/3d.html
  Date: 2026-08-27
  Browser 3D CNN for handwritten digit recognition (MNIST-style). You
  draw a digit on a canvas; it is downsampled to a small grayscale grid
  and pushed through a fixed network whose weights are embedded in the
  page. Architecture on the page: input 32×32 = 1024 nodes, conv1
  28×28×6 with 5×5 filters, max-pool to 14×14×6, conv2 10×10×16, pool
  to 5×5×16, then fully-connected 120 and 100, then 10 outputs for
  digits 0–9. The scene draws every neuron as a small cube (cubes.js /
  Three.js), colored by activation, with switches to hide or show each
  layer. Hover a cube to see its linked inputs highlighted as wireframe
  edges, plus a side panel with the filter patch, the weighted input,
  the arithmetic (scaled tanh) and the output value. Formal details on
  the project index: https://adamharley.com/nn_vis/.
- **Feature Visualization — Distill (Olah, Mordvintsev, Schubert, 2017) — detailed re-ingest**
  https://distill.pub/2017/feature-visualization/
  Date: 2026-08-27 (first ingested 2026-08-24 as short entry under Core CNN Reading; detailed version kept here as potential source update)
  Distill article from Nov 7, 2017 on how GoogLeNet trained on ImageNet
  builds its sense of images layer by layer. Main ideas in own words:
  feature visualization by optimization — start from noise and nudge pixels
  by gradient to make a chosen neuron, channel, whole layer (DeepDream),
  or class logit / probability fire. Class logits before softmax give
  cleaner images than probabilities after softmax. Why optimize instead of
  just searching the dataset: optimization separates true causes from
  correlated context and lets you probe joint behavior. Diversity: one
  optimization tends to show one facet; the authors add a diversity term
  (penalizing cosine similarity of Gram matrices across examples, borrowed
  from style transfer) and also discuss earlier tricks like clustering
  activations or starting from diverse dataset patches and newer
  generator-based sampling. Interaction: neurons are basis vectors of an
  activation space; random directions can also look meaningful, and
  arithmetic on neurons (e.g., adding channels) or interpolating between
  objectives reveals how features combine. The enemy is high-frequency
  noise and checkerboard artifacts from strided convolution and pooling
  gradients, which dominate unregularized results and look like
  adversarial examples. Regularization spectrum: weak (frequency
  penalization by total variation or blurring each step; bilateral
  filters), medium (transformation robustness — jitter, rotate, scale
  before each step), strong (learned priors — GAN/VAE generators or
  denoising autoencoder priors, patch priors). Preconditioning and
  parameterization: blurring the gradient is not a regularizer but a
  change of basis; the paper advocates Fourier decorrelation with color
  decorrelation (Cholesky on training-set color covariance) and Adam for
  2560 steps with padding/crop jitter and small scales/rotations. All
  figures in the article use that decorrelated Fourier setup. Comes with
  appendix visualizing every GoogLeNet channel and open code at
  tensorflow/lucid.
- **AI Vision Explained (and How to Avoid Paying for It) — FortNine | 806 — only relevant parts**
  https://www.youtube.com/watch?v=pqO1WeRigq8
  Date: 2026-08-27
  Relevant segment approx 00:44–07:30 and 07:50–09:00; remainder is a
  sponsored demo of the Insta360 Ace Pro 2 and motorcycle-culture commentary,
  not used here. Core content used: an image is a matrix of RGB pixels;
  a kernel (small matrix) slides across it, dot product at each overlap
  (convolution). Example vertical-edge kernel with negative weights on one
  side and positive on the other gives zero on flat regions and a strong
  response on a vertical edge; same idea extends to horizontal edges and
  other traits. Stacking such operations turns edges into shapes, shapes
  into parts (eye, mouth), parts into arrangements that score as a face —
  a convolutional neural network as a long chain of learned filters. Then
  the shift from hand-crafted feature engineering (a few dozen kernels by
  hand) to learning: start from random kernels, have crowd-labeled data,
  define a cost function as the gap between random output and true label,
  and follow the slope downhill (gradient descent) to find kernels that
  lower cost; depth comes from thousands of such kernels in many layers.
  The video also notes the black-box side effect: thousands of hidden
  kernels give a logic that works but is hard for a person to retrace,
  so mistakes look unhuman though rarer. Caps transcript is noisy
  (auto-captions split lines and mishear words); summary above paraphrases.
  Source meta: FortNine, 2024-10-22, duration 13:26.
- **NotebookLM — Comprehensive Guide (based on Aurélien Géron, Hands-On Machine Learning)**
  https://notebook.google.com/notebook/9e3bcac0-163a-465a-8167-63a63ad00dc7
  Date: 2026-08-27
  NotebookLM notebook that packages Aurélien Géron's book as a study
  companion. In own words: it walks from first ideas such as linear
  regression and decision trees to modern deep nets including transformers
  and GANs, using the Python stack Scikit-Learn, Keras and TensorFlow with
  a hands-on focus. It follows the full project path from cleaning and
  preparing data through training to putting a model into service and
  scaling it, aimed at readers who already code at a basic level and want
  to see how machines learn from data to solve real tasks. Consider for
  bridging the CNN chapters to end-to-end pipelines and deployment notes;
  not yet vetted for intranet use.
