# Weighted Ensemble

## Overview

This folder contains the weighted ensemble implementation used to combine predictions from the best-performing individual models in the chest X-ray classification study.

The ensemble combines class-probability outputs from:

* DenseNet-121
* CovidNet CXR-2
* Attention ResNet

The goal is to improve final classification performance by weighting each model according to its validation accuracy.

---

## Ensemble Summary

* Ensemble Type: Weighted probability ensemble
* Models Combined:

  * DenseNet-121
  * CovidNet CXR-2
  * Attention ResNet
* Input: Saved model predictions on the test dataset
* Output: Final ensemble prediction
* Number of Classes: 3

  * Normal
  * COVID-19
  * Pneumonia

---

## Performance

| Metric        | Value  |
| ------------- | ------ |
| Test Accuracy | 95.85% |
| Precision     | 96%    |
| Recall        | 96%    |
| F1 Score      | 96%    |

### Class-Level Results

| Class     | Precision | Recall | F1 Score | Support |
| --------- | --------- | ------ | -------- | ------- |
| Normal    | 0.90      | 0.98   | 0.94     | 280     |
| COVID-19  | 0.98      | 0.99   | 0.99     | 320     |
| Pneumonia | 0.99      | 0.90   | 0.94     | 315     |

---

## Folder Structure

```text
W-ensemble/
├── attenresnet.pkl
├── covidnet.pkl
├── densenet.pkl
├── dataloader.py
├── test_p_atten.npy
├── test_p_covid.npy
├── test_p_dens.npy
├── h_ensemble.png
└── w-ensemble.ipynb
```

### attenresnet.pkl

Saved training history for the Attention ResNet model.

### covidnet.pkl

Saved training history for the CovidNet model.

### densenet.pkl

Saved training history for the DenseNet model.

### dataloader.py

Dataset loading and label preparation utilities.

### test_p_atten.npy

Saved Attention ResNet predictions on the test dataset.

### test_p_covid.npy

Saved CovidNet predictions on the test dataset.

### test_p_dens.npy

Saved DenseNet predictions on the test dataset.

### h_ensemble.png

Confusion matrix generated for the final weighted ensemble model.

### w-ensemble.ipynb

Main notebook implementing the weighted ensemble pipeline and evaluation.

---

## Notebook Imports

The notebook uses:

```python
import pickle
import numpy as np
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

from dataloader import *
```

---

## Ensemble Method

The ensemble weights are computed from the best validation accuracy of each model.

First, the best validation accuracy is extracted:

```python
acc_dens = max(densnet['val_accuracy'])
acc_cov = max(covidnet['val_accuracy'])
acc_res = max(residual_attention['val_accuracy'])
```

Then the minimum validation accuracy is used as a baseline:

```python
beta = min(acc_dens, acc_cov, acc_res)
```

Model weights are calculated as:

```python
alfa_dens = acc_dens - beta
alfa_cov = acc_cov - beta
alfa_res = acc_res - beta
```

The final ensemble prediction is obtained by weighted summation of model probabilities:

```python
ensemble = test_dens * alfa_dens + test_cov * alfa_cov + test_res * alfa_res
```

The final predicted class is selected using:

```python
test_value_max = np.argmax(ensemble, axis=1)
```

---

## Evaluation

The ensemble is evaluated using:

* Accuracy
* Precision
* Recall
* F1 score
* Confusion matrix

The final ensemble achieved **95.85% test accuracy**, slightly improving over the best standalone model, DenseNet-121.

---

## Key Observation

The ensemble achieved the best overall performance in the study. However, the improvement over DenseNet alone was modest.

This suggests that the individual models shared similar decision boundaries and failure modes, especially for pneumonia classification.

---

## Results Within the Full Study

The weighted ensemble was compared against:

* Attention ResNet 1
* Attention ResNet 2
* CovidNet
* DenseNet

The final ensemble achieved the highest test accuracy:

| Model              | Test Accuracy |
| ------------------ | ------------- |
| Attention ResNet 1 | 89.29%        |
| Attention ResNet 2 | 91.48%        |
| CovidNet           | 94.10%        |
| DenseNet           | 95.74%        |
| Weighted Ensemble  | 95.85%        |

---

## Reference

For a detailed description of the ensemble method, training histories, and evaluation procedure, see the full project report available in the repository root.
