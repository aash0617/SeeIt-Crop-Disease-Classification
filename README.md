# 🌿 SeeIt – Crop Leaf Disease Classification

<p align="center">

### Intelligent Crop Leaf Disease Classification using Deep Learning and Transfer Learning

**Dataset:** PlantVillage + Custom Leaf Detector Dataset  
**Framework:** PyTorch  
**Models:** MobileNetV2 + Leaf Detector

</p>

---

# 📖 Project Overview

**SeeIt** is a deep learning-based computer vision application that automatically identifies crop leaf diseases from images.

The project follows a **two-stage prediction pipeline**:

1. **Leaf Detection**
   - Determines whether the uploaded image contains a leaf.
   - Prevents incorrect disease predictions for images that do not contain leaves.

2. **Disease Classification**
   - If a leaf is detected, the image is classified into one of the **38 PlantVillage disease classes** using a MobileNetV2 transfer learning model.

The application is deployed using **Streamlit**, allowing users to upload an image and receive disease predictions with confidence scores and disease information.

---

# 🎯 Project Objectives

- Detect whether an uploaded image contains a plant leaf.
- Prevent invalid predictions for non-leaf images.
- Classify crop leaf diseases using Transfer Learning.
- Build an efficient and lightweight prediction pipeline.
- Deploy the model using Streamlit.
- Assist farmers and researchers with early disease identification.

---

# 🌱 Datasets

## 1. PlantVillage Dataset

The PlantVillage dataset is used for crop disease classification.

### Dataset Details

- Dataset: PlantVillage
- Number of Classes: **38**
- Total Images: **54,000+**
- Image Format: JPEG
- Image Size: 256 × 256

The disease classifier is trained using the **Color** version of the PlantVillage dataset.

---

## 2. Custom Leaf Detector Dataset

A custom dataset was created for detecting whether an uploaded image contains a leaf.

### Classes

- Leaf
- Non-Leaf

This model acts as a preprocessing stage before disease prediction.

---

# 🔄 Project Workflow

```
User Uploads Image
        │
        ▼
Leaf Detector
        │
        ├── Non-Leaf
        │       │
        │       ▼
        │  Display:
        │ "Please upload a leaf image."
        │
        ▼
Leaf Detected
        │
        ▼
Image Preprocessing
        │
        ▼
MobileNetV2 Disease Classifier
        │
        ▼
Predicted Disease
        │
        ▼
Confidence Score
        │
        ▼
Disease Information
        │
        ▼
Displayed in Streamlit
```

---

# 📂 Repository Structure

```
SeeIt-Crop-Disease-Classification/
│
├── app/
│   └── app.py
│
├── data/
│   └── color/
│
├── docs/
│   └── design_doc.md
│
├── models/
│   ├── leaf_detector.pth
│   └── mobilenet_plant_disease_new.pth
│
├── notebooks/
│   ├── 01_data_check.ipynb
│   ├── 02_data_preprocessing.ipynb
│   ├── 03_mobilenetv2_training.ipynb
│   ├── 04_prediction.ipynb
│   └── 05_leaf_detector.ipynb
│
├── src/
│   ├── disease_info.py
│   ├── leaf_detector.py
│   ├── predict.py
│   └── preprocess.py
│
├── split_dataset.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

# 🚀 Features

- Leaf vs Non-Leaf Detection
- Disease Classification
- Transfer Learning with MobileNetV2
- Confidence Score Display
- Disease Information Display
- Image Upload Interface
- Streamlit Web Application
- PyTorch Implementation
- Custom Leaf Detection Model

---

# 🛠 Technologies Used

| Category | Technology |
|-----------|------------|
| Programming Language | Python |
| Deep Learning | PyTorch |
| Computer Vision | TorchVision |
| Image Processing | Pillow (PIL) |
| Visualization | Matplotlib |
| Web Framework | Streamlit |
| Development | Jupyter Notebook |
| Version Control | Git & GitHub |

---

# 🧠 Deep Learning Approach

## Stage 1 – Leaf Detector

A lightweight binary image classifier determines whether the uploaded image contains:

- Leaf
- Non-Leaf

If the uploaded image is classified as **Non-Leaf**, disease prediction is stopped and the user is asked to upload a valid leaf image.

---

## Stage 2 – Disease Classifier

The disease classifier uses **Transfer Learning** with **MobileNetV2**, pretrained on ImageNet.

The final classification layer is modified to classify the **38 PlantVillage disease classes**.

This approach provides:

- Faster convergence
- Better accuracy
- Lower computational cost
- Efficient deployment

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/aash0617/SeeIt-Crop-Disease-Classification.git
```

Move to the project directory

```bash
cd SeeIt-Crop-Disease-Classification
```

Install the dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app/app.py
```

---

# 📄 Note

- The PlantVillage dataset is **not included** in this repository because of its large size.
- The custom leaf detector dataset is also excluded using `.gitignore`.
- Both datasets must be downloaded locally before training.

---

# 👩‍💻 Author

**Aastha Bhalla**

B.Tech – Computer Science and Engineering (AI & Data Engineering)

Lovely Professional University
