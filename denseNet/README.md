# DenseNet-121

## Overview

This folder contains the implementation of DenseNet-121 used in the chest X-ray classification study.

DenseNet introduces dense connectivity between layers, enabling efficient feature reuse and improved gradient propagation throughout the network. Among all evaluated architectures, DenseNet achieved the strongest standalone performance on the chest X-ray classification task.

---

## Model Summary

* Architecture: DenseNet-121
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
| Test Accuracy | 95.74% |
| Precision     | 96%    |
| Recall        | 96%    |
| F1 Score      | 96%    |

---

## Folder Structure

```text
denseNet/
├── dataloader.py
├── densenet.py
├── train.py
└── densenet.ipynb
```

### dataloader.py

Dataset loading, preprocessing, augmentation, and data preparation utilities.

### densenet.py

Implementation of the DenseNet-121 architecture used in this project.

### train.py

Training and evaluation utilities used by the notebook workflow.

### densenet.ipynb

Main notebook integrating data loading, model construction, training, and evaluation.

The notebook imports:

```python
from dataloader import *
from densenet import densenet
from train import *
```

---

## Training Configuration

| Parameter              | Value             |
| ---------------------- | ----------------- |
| Optimizer              | Adam              |
| Initial Learning Rate  | 0.001             |
| Batch Size             | 32                |
| Epochs                 | 150               |
| Learning Rate Schedule | ReduceLROnPlateau |
| Early Stopping         | Enabled           |

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

## Key Observation

DenseNet achieved the highest standalone performance among all investigated architectures while maintaining a favorable balance between predictive accuracy, computational complexity, and training time.

The dense connectivity pattern enables efficient information flow between layers and appears particularly effective for this medical image classification task.

---

## Related Work

This implementation is based on:

> Huang et al., "Densely Connected Convolutional Networks", CVPR 2017.

https://arxiv.org/abs/1608.06993

---

## Results Within the Full Study

DenseNet was compared against:

* CovidNet CXR-2
* Attention ResNet (Version 1)
* Attention ResNet (Version 2)
* Weighted Ensemble

DenseNet achieved the strongest standalone performance with a test accuracy of **95.74%**, while the final weighted ensemble achieved **95.85%**.

---

## Reference

For a detailed description of the architecture, training procedure, and evaluation methodology, see the full project report available in the repository root.
