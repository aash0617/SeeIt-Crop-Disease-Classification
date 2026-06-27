# 🌿 SeeIt – Crop Leaf Disease Classification

<div align="center">

### Intelligent Crop Leaf Disease Detection using Deep Learning and Transfer Learning

**Dataset:** PlantVillage  
**Framework:** PyTorch  
**Model:** MobileNetV2 (Transfer Learning)

</div>

---

# 📖 Project Overview

SeeIt is a deep learning-based image classification system designed to identify diseases in crop leaves using computer vision techniques. The project leverages the PlantVillage dataset and a pretrained MobileNetV2 model to accurately classify leaf images into healthy or diseased categories.

The primary objective of this project is to build an efficient, lightweight, and scalable disease classification model that can later be integrated into a web application for real-world agricultural use.

---

# 🎯 Objectives

- Develop an automated crop disease classification system.
- Reduce dependency on manual disease identification.
- Utilize Transfer Learning to improve model performance.
- Compare the effectiveness of different image representations.
- Build a deployable solution using Streamlit.

---

# 🌱 Dataset

The project uses the **PlantVillage Dataset**, one of the most widely used datasets for plant disease classification.

### Dataset Variants

- 🌈 Color Images
- ⚫ Grayscale Images
- ✂️ Segmented Images

### Dataset Information

- Total Classes: **38**
- Total Images: **54,000+**
- Image Format: JPEG
- Image Size: 256 × 256

During the initial phase, development is performed using the **Color Dataset**, after which the same pipeline will be extended to the Grayscale and Segmented datasets for comparison.

---

# 🏗 Project Architecture

```
PlantVillage Dataset
        │
        ▼
Dataset Verification
        │
        ▼
Image Preprocessing
        │
        ▼
Data Augmentation
        │
        ▼
PyTorch Dataset
        │
        ▼
DataLoader
        │
        ▼
MobileNetV2
        │
        ▼
Disease Prediction
        │
        ▼
Streamlit Web Application
```

---

# ⚙️ Features

- Dataset exploration and verification
- Image preprocessing pipeline
- Image normalization
- Data augmentation
- PyTorch Dataset and DataLoader
- Transfer Learning using MobileNetV2
- Disease prediction
- Lightweight architecture suitable for deployment

---

# 🛠 Technologies Used

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Framework | PyTorch |
| Computer Vision | TorchVision |
| Image Processing | PIL (Pillow) |
| Visualization | Matplotlib |
| Development | Jupyter Notebook |
| Deployment | Streamlit |

---

# 📂 Repository Structure

```
SeeIt-Crop-Disease-Classification/

│── app/
│── data/
│── docs/
│── models/
│── notebooks/
│     ├── 01_data_check.ipynb
│     ├── 02_data_preprocessing.ipynb
│
│── src/
│── README.md
│── .gitignore
```

---

# ✅ Current Progress

- Repository initialized
- Project structure created
- Design documentation completed
- Dataset verified
- Image analysis completed
- Class distribution explored
- Image preprocessing pipeline implemented
- Data augmentation pipeline created
- PyTorch Dataset and DataLoader implemented

---

# 🔬 Deep Learning Model

The project utilizes **MobileNetV2**, a lightweight convolutional neural network optimized for efficient image classification.

Instead of training a model from scratch, **Transfer Learning** is employed by using pretrained ImageNet weights and adapting the final classification layer to classify the PlantVillage dataset.

---

# 📌 Note

The PlantVillage dataset is **not included** in this repository because of its large size. It is excluded through `.gitignore`.

---

# 👩‍💻 Author

**Aastha Bhalla**

B.Tech Computer Science Engineering (AI & Data Engineering)

Lovely Professional University

---

## ⭐ If you found this project interesting, consider giving it a star!
