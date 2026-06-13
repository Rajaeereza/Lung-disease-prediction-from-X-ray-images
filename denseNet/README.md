# DenseNet-121

## Overview

This folder contains the implementation of DenseNet-121 used for chest X-ray classification.

DenseNet introduces direct connections between layers, enabling efficient feature reuse and improved gradient flow throughout the network. This architecture achieved the strongest standalone performance among all evaluated models.

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

## Contents

This folder contains:

* DenseNet architecture implementation
* Training notebooks
* Evaluation notebooks
* Saved model checkpoints (if available)

---

## Key Observation

DenseNet achieved the highest standalone performance while maintaining a favorable balance between predictive accuracy, training time, and model complexity.
