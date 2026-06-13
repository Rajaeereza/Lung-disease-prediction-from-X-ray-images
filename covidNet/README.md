# CovidNet CXR-2

## Overview

This folder contains the implementation of CovidNet CXR-2 used in the chest X-ray classification study.

CovidNet is a lightweight deep convolutional neural network specifically designed for COVID-19 detection from chest X-ray images. The architecture employs Projection-Replication-Projection-Expansion (PRPE) blocks to improve representational capacity while maintaining computational efficiency.

Among the evaluated architectures, CovidNet achieved competitive performance with fewer learnable parameters than DenseNet and Attention ResNet.

---

## Model Summary

* Architecture: CovidNet CXR-2
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
| Test Accuracy | 94.10% |
| Precision     | 94%    |
| Recall        | 94%    |
| F1 Score      | 94%    |

---

## Folder Structure

```text id="p7ekwy"
covidNet/
├── covidnet.py
├── dataloader.py
├── train.py
└── covidnet.ipynb
```

### dataloader.py

Dataset loading, preprocessing, augmentation, and data preparation utilities.

### covidnet.py

Implementation of the CovidNet CXR-2 architecture, including the PRPE blocks and network structure.

### train.py

Training and evaluation utilities used by the notebook workflow.

### covidnet.ipynb

Main notebook integrating data loading, model construction, training, and evaluation.

The notebook imports:

```python id="8n0slh"
from dataloader import *
from covidnet import covidnet
from train import *
```

---

## Training Configuration

| Parameter              | Value             |
| ---------------------- | ----------------- |
| Optimizer              | Adam              |
| Initial Learning Rate  | 0.0002            |
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

## Architecture Highlights

CovidNet was originally developed for COVID-19 detection from chest X-ray images and introduces:

* Projection-Replication-Projection-Expansion (PRPE) blocks
* Lightweight architecture design
* Reduced computational complexity
* Strategic long-range connectivity
* Efficient feature extraction for medical imaging tasks

Compared with densely connected architectures, CovidNet uses a smaller number of learnable parameters while maintaining strong classification performance.

---

## Key Observation

CovidNet achieved strong classification performance while maintaining a lower parameter count than the other investigated architectures.

This demonstrates that carefully designed lightweight architectures can remain highly competitive on medical imaging tasks without requiring excessive model complexity.

---

## Related Work

This implementation is based on:

> Pavlova et al., "COVID-Net CXR-2: An Enhanced Deep Convolutional Neural Network Design for Detection of COVID-19 Cases From Chest X-ray Images", Frontiers in Medicine, 2022.

---

## Results Within the Full Study

CovidNet was compared against:

* DenseNet-121
* Attention ResNet (Version 1)
* Attention ResNet (Version 2)
* Weighted Ensemble

CovidNet achieved a test accuracy of **94.10%**, demonstrating competitive performance while maintaining a compact architecture.

---

## Reference

For a detailed description of the architecture, training procedure, and evaluation methodology, see the full project report available in the repository root.
