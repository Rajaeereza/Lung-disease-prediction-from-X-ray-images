# Attention ResNet (Version 2)

## Overview

This folder contains the second implementation of the Residual Attention Network used in the chest X-ray classification study.

Building upon the first Attention ResNet implementation, modifications were introduced to the residual-unit configuration to improve optimization stability and classification performance.

The objective was to investigate whether architectural refinements could improve feature learning and overall predictive performance for chest X-ray classification.

---

## Model Summary

* Architecture: Modified Residual Attention Network
* Training Strategy: Trained from scratch
* Input Resolution: 224 × 224
* Number of Classes: 3

  * Normal
  * COVID-19
  * Pneumonia

---

## Performance

| Metric        | Value  |
| ------------- | ------ |
| Test Accuracy | 91.48% |
| Precision     | 91%    |
| Recall        | 91%    |
| F1 Score      | 91%    |

---

## Folder Structure

```text
attention_ResNet_2/
├── atten_resnet.py
├── dataloader.py
├── train.py
└── attention_ResNet_2.ipynb
```

### dataloader.py

Dataset loading, preprocessing, augmentation, and data preparation utilities.

### atten_resnet.py

Implementation of the modified Residual Attention Network architecture, including attention modules and residual blocks.

### train.py

Training and evaluation utilities used by the notebook workflow.

### attention_ResNet_2.ipynb

Main notebook integrating data loading, model construction, training, and evaluation.

The notebook imports:

```python
from dataloader import *
from atten_resnet import atten_resnet
from train import *
```

---

## Training Configuration

| Parameter               | Value                                      |
| ----------------------- | ------------------------------------------ |
| Optimizer               | Nesterov SGD                               |
| Weight Decay            | 0.0001                                     |
| Momentum                | 0.9                                        |
| Initial Learning Rate   | 0.0001                                     |
| Batch Size              | 32                                         |
| Epochs                  | 150                                        |
| Learning Rate Schedule  | LearningRateScheduler                      |
| Learning Rate Update    | Learning rate divided by 2 every 30 epochs |
| Early Stopping Patience | 30                                         |


---

## Experimental Setup

The model was trained on chest X-ray images belonging to three classes:

* COVID-19
* Pneumonia
* Normal

All images were:

* Resized to 224 × 224 pixels
* Normalized
* Augmented using random transformations including rotation, shifts, zooming, horizontal flipping, and brightness adjustments

---

## Architecture Highlights

The modified Residual Attention Network combines:

* Residual learning
* Attention mechanisms
* Hierarchical feature extraction
* Deep convolutional representations
* Revised residual-unit configuration

The attention modules are designed to emphasize diagnostically relevant image regions while suppressing irrelevant information during feature extraction.

---

## Key Observation

The modifications introduced in Version 2 improved classification performance from **89.29%** to **91.48%**, demonstrating that architectural design choices within the residual-attention framework can significantly affect optimization and predictive accuracy.

Although DenseNet and CovidNet still achieved higher overall performance, Version 2 showed clear improvements over the original implementation.

---

## Related Work

This implementation is based on:

> Wang et al., "Residual Attention Network for Image Classification", CVPR 2017.

https://arxiv.org/abs/1704.06904

---

## Results Within the Full Study

Attention ResNet (Version 2) was compared against:

* DenseNet-121
* CovidNet CXR-2
* Attention ResNet (Version 1)
* Weighted Ensemble

The model achieved a test accuracy of **91.48%**, improving upon the original Attention ResNet implementation by approximately **2.2 percentage points**.

---

## Reference

For a detailed description of the architecture, training procedure, and evaluation methodology, see the full project report available in the repository root.
