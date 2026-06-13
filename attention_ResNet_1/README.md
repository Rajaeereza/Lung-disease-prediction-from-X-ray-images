# Attention ResNet (Version 1)

## Overview

This folder contains the first implementation of the Residual Attention Network used in the chest X-ray classification study.

Residual Attention Networks combine residual learning with attention mechanisms that guide feature extraction toward informative regions of an image. The objective is to improve representation learning by allowing the network to focus on diagnostically relevant features while suppressing less informative information.

This implementation represents the initial Attention ResNet architecture evaluated in the study.

---

## Model Summary

- Architecture: Residual Attention Network
- Training Strategy: Trained from scratch
- Input Resolution: 224 × 224
- Number of Classes: 3
  - Normal
  - COVID-19
  - Pneumonia

---

## Performance

| Metric | Value |
|----------|----------|
| Test Accuracy | 89.29% |
| Precision | 89% |
| Recall | 89% |
| F1 Score | 89% |

---

## Folder Structure

attention_ResNet_1/
├── atten_resnet.py
├── dataloader.py
├── train.py
└── attention_ResNet_1.ipynb

### dataloader.py

Dataset loading, preprocessing, augmentation, and data preparation utilities.

### atten_resnet.py

Implementation of the Residual Attention Network architecture, including attention modules and residual blocks.

### train.py

Training and evaluation utilities used by the notebook workflow.

### attention_ResNet_1.ipynb

Main notebook integrating data loading, model construction, training, and evaluation.

The notebook imports:

from dataloader import *
from atten_resnet import atten_resnet
from train import *

---

## Training Configuration

| Parameter | Value |
|------------|------------|
| Optimizer | Adam |
| Initial Learning Rate | (verify from notebook/report) |
| Batch Size | (verify from notebook/report) |
| Epochs | (verify from notebook/report) |
| Learning Rate Schedule | ReduceLROnPlateau |
| Early Stopping | Enabled |

---

## Experimental Setup

The model was trained on chest X-ray images belonging to three classes:

- COVID-19
- Pneumonia
- Normal

All images were:

- Resized to 224 × 224 pixels
- Normalized
- Augmented using random transformations including rotation, shifts, zooming, horizontal flipping, and brightness adjustments

---

## Architecture Highlights

The Residual Attention Network combines:

- Residual learning
- Attention mechanisms
- Hierarchical feature extraction
- Deep convolutional representations

The attention modules are designed to emphasize informative image regions and suppress irrelevant background information during training.

---

## Key Observation

Although the architecture successfully learned meaningful image representations, its performance was lower than DenseNet and CovidNet in this study.

This motivated further architectural modifications explored in the second Attention ResNet implementation.

---

## Related Work

Wang et al., Residual Attention Network for Image Classification (CVPR 2017)

https://arxiv.org/abs/1704.06904

---

## Results Within the Full Study

Attention ResNet (Version 1) was compared against:

- DenseNet-121
- CovidNet CXR-2
- Attention ResNet (Version 2)
- Weighted Ensemble

The model achieved a test accuracy of 89.29% and served as the baseline attention-based architecture for subsequent improvements.

---

## Reference

For a detailed description of the architecture, training procedure, and evaluation methodology, see the full project report available in the repository root.
