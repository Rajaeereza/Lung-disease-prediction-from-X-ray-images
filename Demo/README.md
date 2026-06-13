# Demo

## Overview

This folder contains the demonstration notebook for running inference with the trained chest X-ray classification models.

The demo evaluates trained DenseNet, CovidNet, Attention ResNet, and ensemble predictions on a small demonstration subset of chest X-ray images.

The purpose of this folder is to show how the trained models can be loaded, used for prediction, and evaluated on example data.

---

## Demo Summary

* Task: Chest X-ray classification demo
* Models Used:

  * DenseNet-121
  * CovidNet CXR-2
  * Attention ResNet
  * Weighted Ensemble
* Input Resolution: 224 × 224
* Number of Classes: 3

  * Normal
  * COVID-19
  * Pneumonia
* Demo Set Size: 50 images

---

## Folder Structure

```text
Demo/
├── atten.index
├── atten_resnet.py
├── covid.index
├── covidnet.pkl
├── covidnet.py
├── dataloader.py
├── demo.ipynb
├── dense.index
├── densenet.py
├── pneumonia_class.png
├── test_p_atten.npy
└── test_p_dens.npy
```

### demo.ipynb

Main demonstration notebook for loading trained models, running inference, visualizing sample images, and evaluating predictions.

### dataloader.py

Dataset loading and preprocessing utilities.

### densenet.py

DenseNet-121 architecture implementation.

### covidnet.py

CovidNet CXR-2 architecture implementation.

### atten_resnet.py

Attention ResNet architecture implementation.

### dense.index

Saved DenseNet checkpoint index file.

### covid.index

Saved CovidNet checkpoint index file.

### atten.index

Saved Attention ResNet checkpoint index file.

### covidnet.pkl

Saved CovidNet training history.

### test_p_atten.npy

Saved Attention ResNet prediction outputs.

### test_p_dens.npy

Saved DenseNet prediction outputs.

### pneumonia_class.png

Example visualization of pneumonia-class chest X-ray images generated from the demo notebook.

---

## Notebook Imports

The notebook uses:

```python
import tensorflow as tf
import numpy as np
import pickle
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.optimizers import RMSprop
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

from dataloader import *
from densenet import densenet
from covidnet import covidnet
from atten_resnet import atten_resnet
from train import *
```

---

## Dataset Setup

The demo notebook was designed to run in Google Colab.

The dataset is loaded from Google Drive after mounting:

```python
from google.colab import drive
drive.mount('/content/drive')
```

Example dataset paths used in the notebook:

```python
path_metadata = "/content/drive/MyDrive/dataset/metadata.csv"
path_pneumonia = "/content/drive/MyDrive/dataset/Dataset/pneumonia"
directory_dataset = "/content/drive/MyDrive/dataset/Dataset"
```

Input configuration:

```python
image_size = (224, 224)
batch_size = 32
```

---

## Demo Workflow

The notebook performs the following steps:

1. Mount Google Drive.
2. Load the dataset using `data_func`.
3. Visualize sample chest X-ray images from each class.
4. Load trained model weights.
5. Run inference using:

   * DenseNet
   * CovidNet
   * Attention ResNet
6. Evaluate each model on the demo dataset.
7. Compute ensemble predictions.
8. Generate classification reports and confusion matrices.

---

## Demo Results

### DenseNet

| Metric        | Value |
| ------------- | ----- |
| Demo Accuracy | 100%  |

### CovidNet

| Metric        | Value |
| ------------- | ----- |
| Demo Accuracy | 98%   |

### Attention ResNet

| Metric        | Value |
| ------------- | ----- |
| Demo Accuracy | 98%   |

### Ensemble

| Metric        | Value |
| ------------- | ----- |
| Demo Accuracy | 100%  |

---

## Important Note

The demo results are computed on a small subset of 50 images and should not be interpreted as the main experimental result.

The main evaluation results are reported on the full test set of 915 images in the project report and main repository README.

---

## Ensemble Demonstration

The demo notebook also computes an ensemble prediction using validation-accuracy-based weighting.

Example validation accuracies used in the demo:

```text
DenseNet: 0.9616
CovidNet: 0.9233
Attention ResNet: 0.9162
```

The resulting weights are computed relative to the lowest validation accuracy.

---

## Key Observation

The demo notebook provides a practical example of how the trained models can be loaded and evaluated.

It is useful for understanding the inference workflow, but the full test-set evaluation should be used for reporting final model performance.

---

## Reference

For complete training details, model comparison, and final test-set results, see the full project report available in the repository root.
