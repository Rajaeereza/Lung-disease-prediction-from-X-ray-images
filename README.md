# Ensemble Learning for Chest X-Ray Classification

## Overview

This project investigates the application of deep learning methods for automated chest X-ray classification. Three convolutional neural network architectures—DenseNet-121, CovidNet CXR-2, and Attention ResNet—were implemented and trained from scratch to classify chest X-ray images into three diagnostic categories:

* Normal
* COVID-19
* Pneumonia

To leverage the complementary strengths of the individual models, a weighted ensemble strategy was developed and evaluated.

The project was completed as part of the Master's Degree in Physics of Data at the University of Padova.

---

## Research Highlights

* Implemented and trained all models from scratch
* Compared three fundamentally different CNN architectures
* Evaluated ensemble learning for medical image classification
* Achieved **95.85% test accuracy**
* Performed comparative analysis of model strengths and weaknesses
* Investigated classification errors across disease categories

---

## Workflow

```text
Chest X-Ray Dataset
          │
          ▼
    Preprocessing
 (Resize + Normalize +
    Augmentation)
          │
          ├──────────────┬──────────────┬──────────────┐
          ▼              ▼              ▼
      DenseNet       CovidNet    Attention ResNet
          │              │              │
          └──────────────┴──────────────┘
                         │
                         ▼
                Weighted Ensemble
                         │
                         ▼
                Final Prediction
```

---

## Dataset

The study uses the **COVID-19, Pneumonia and Normal Chest X-ray PA Dataset** from Mendeley Data.

Dataset link:

https://data.mendeley.com/datasets/jctsfj2sfn/1

### Dataset Statistics

| Class     | Images |
| --------- | ------ |
| COVID-19  | 1525   |
| Pneumonia | 1525   |
| Normal    | 1525   |
| Total     | 4575   |

### Data Split

| Subset     | Samples |
| ---------- | ------- |
| Training   | 2928    |
| Validation | 732     |
| Test       | 915     |

### Preprocessing

All images were:

* Resized to 224 × 224 pixels
* Normalized using dataset statistics
* One-hot encoded

Data augmentation included:

* Random rotation
* Width shift
* Height shift
* Zoom
* Horizontal flip
* Brightness variation

---

## Methods

### DenseNet-121

DenseNet introduces dense connectivity between layers, allowing feature reuse and improved gradient propagation throughout the network.

### CovidNet CXR-2

CovidNet is a lightweight architecture specifically designed for COVID-19 detection from chest X-ray images. It uses Projection-Replication-Projection-Expansion (PRPE) blocks to balance efficiency and representational power.

### Attention ResNet

Attention ResNet incorporates attention modules that guide feature extraction by emphasizing informative image regions during training.

### Weighted Ensemble

Predictions from the best-performing models were combined using a weighted ensemble approach. Model weights were determined from validation performance and used to aggregate class probabilities.

---

## Results

### Model Comparison

| Model              | Test Accuracy |
| ------------------ | ------------- |
| Attention ResNet 1 | 89.29%        |
| Attention ResNet 2 | 91.48%        |
| CovidNet           | 94.10%        |
| DenseNet-121       | 95.74%        |
| Weighted Ensemble  | **95.85%**    |

### Additional Metrics

| Model        | Precision | Recall | F1 Score |
| ------------ | --------- | ------ | -------- |
| DenseNet-121 | 96%       | 96%    | 96%      |
| Ensemble     | 96%       | 96%    | 96%      |

---

## Key Findings

### DenseNet was the strongest individual model

DenseNet achieved the highest standalone performance while maintaining reasonable computational complexity.

### Ensemble learning produced only a modest improvement

The weighted ensemble improved accuracy from 95.74% to 95.85%.

This suggests that despite architectural differences, the models learned similar decision boundaries and shared several failure modes.

### Pneumonia remained the most challenging class

All architectures showed difficulties distinguishing pneumonia from normal chest X-rays, indicating that improved data quality, larger datasets, or additional diagnostic information may be required.

---

## Repository Structure

```text
.
├── denseNet/
├── covidNet/
├── attention_ResNet_1/
├── attention_ResNet_2/
├── W-ensemble/
├── Demo/
├── figures/
├── report/
├── requirements.txt
└── README.md
```

### denseNet/

Implementation of DenseNet-121 and related training scripts.

### covidNet/

Implementation of CovidNet CXR-2.

### attention_ResNet_1/

First Attention ResNet implementation.

### attention_ResNet_2/

Modified Attention ResNet architecture with improved performance.

### W-ensemble/

Weighted ensemble framework combining model predictions.

### Demo/

Example notebooks for model inference and evaluation.

---

## How to Run

### 1. Clone Repository

```bash
git clone https://github.com/your-username/Ensemble-Learning-for-Chest-XRay-Classification.git
cd Ensemble-Learning-for-Chest-XRay-Classification
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Download Dataset

Download the dataset from:

https://data.mendeley.com/datasets/jctsfj2sfn/1

Place the images in the appropriate data directory.

### 4. Train Models

Train any architecture independently:

* DenseNet
* CovidNet
* Attention ResNet

### 5. Run Ensemble Evaluation

After generating predictions from individual models, execute the weighted ensemble pipeline.

---

## Lessons Learned

While the primary objective of this project was classification performance, the experiments highlighted the importance of understanding model failure modes rather than focusing exclusively on accuracy.

The observation that different architectures produced similar classification errors motivated later interests in robustness, representation learning, and trustworthy AI for biomedical applications.

---

## Future Directions

Potential extensions include:

* Grad-CAM visualizations
* Uncertainty estimation
* Calibration analysis
* Out-of-distribution detection
* Explainability comparison across architectures
* Robustness evaluation under dataset shift

---

## References

* Huang et al., DenseNet: Densely Connected Convolutional Networks (CVPR 2017)
* Pavlova et al., COVID-Net CXR-2 (Frontiers in Medicine, 2022)
* Wang et al., Residual Attention Network (2017)

---

## Authors

**Reza Rajaee**
M.Sc. Physics of Data, University of Padova

**Sarvenaz Babakhani**
University of Padova

