# 🌿 SeeIt – Crop Leaf Disease Classification

<p align="center">

### Intelligent Crop Leaf Disease Classification using Deep Learning and Transfer Learning

**Dataset:** PlantVillage  
**Framework:** PyTorch  
**Model:** MobileNetV2 (Transfer Learning)

</p>

---

# 📖 Project Overview

**SeeIt** is a deep learning-based computer vision project that aims to automatically identify crop leaf diseases from images using Transfer Learning. The project utilizes the **PlantVillage** dataset and a pretrained **MobileNetV2** model to classify leaf images into healthy or diseased categories.

The objective of this project is to build a lightweight, efficient, and scalable disease classification system that can later be deployed as a web application to assist farmers and researchers in early disease detection.

---

# 🎯 Project Objectives

- Build an automated crop disease classification system.
- Explore and analyze the PlantVillage dataset.
- Develop a robust image preprocessing pipeline.
- Apply Transfer Learning using MobileNetV2.
- Compare the performance of different image representations.
- Deploy the trained model using Streamlit.

---

# 🌱 Dataset

The project uses the **PlantVillage Dataset**, one of the most popular benchmark datasets for plant disease classification.

### Dataset Variants

- 🌈 Color Images
- ⚫ Grayscale Images
- ✂️ Segmented Images

### Dataset Details

- **Dataset:** PlantVillage
- **Number of Classes:** 38
- **Total Images:** 54,000+
- **Image Format:** JPEG
- **Original Image Size:** 256 × 256 pixels

The implementation begins with the **Color Dataset**, after which the same preprocessing and training pipeline will be extended to the **Grayscale** and **Segmented** datasets for performance comparison.

---

# 🔄 Project Workflow

```
PlantVillage Dataset
        │
        ▼
Dataset Verification
        │
        ▼
Exploratory Data Analysis (EDA)
        │
        ▼
Image Preprocessing
        │
        ├── Resize Images
        ├── Data Augmentation
        ├── Tensor Conversion
        └── Image Normalization
        │
        ▼
PyTorch Dataset & DataLoader
        │
        ▼
Transfer Learning using MobileNetV2
        │
        ▼
Model Training
        │
        ▼
Model Evaluation
        │
        ├── Accuracy
        ├── Precision
        ├── Recall
        ├── F1-Score
        └── Confusion Matrix
        │
        ▼
Model Testing
        │
        ▼
Grad-CAM Visualization
        │
        ▼
Streamlit Web Application
```

---

# 📂 Repository Structure

```
SeeIt-Crop-Disease-Classification/
│
├── app/                             # Streamlit web application
│   ├── app.py
│   ├── prediction.py
│   └── utils.py
│
├── data/                            # Local dataset (ignored by Git)
│   ├── color/
│   ├── grayscale/
│   └── segmented/
│
├── docs/
│   ├── design_doc.md
│   └── project_report.pdf
│
├── models/                          # Saved trained models
│   ├── mobilenetv2_best.pth
│   └── mobilenetv2_final.pth
│
├── notebooks/
│   ├── 01_data_check.ipynb
│   ├── 02_data_preprocessing.ipynb
│   ├── 03_mobilenetv2_training.ipynb
│   ├── 04_model_evaluation.ipynb
│   ├── 05_gradcam_visualization.ipynb
│   └── 06_model_testing.ipynb
│
├── src/
│   ├── dataset.py
│   ├── transforms.py
│   ├── model.py
│   ├── train.py
│   ├── evaluate.py
│   ├── predict.py
│   └── utils.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🚀 Features

- Dataset exploration and verification
- Class distribution analysis
- Image preprocessing pipeline
- Data augmentation
- Image normalization
- PyTorch Dataset creation
- DataLoader implementation
- Transfer Learning using MobileNetV2
- Model evaluation
- Disease prediction
- Streamlit deployment

---

# 🛠 Technologies Used

| Category | Technology |
|-----------|------------|
| Programming Language | Python |
| Deep Learning | PyTorch |
| Computer Vision | TorchVision |
| Image Processing | PIL (Pillow) |
| Visualization | Matplotlib |
| Development Environment | Jupyter Notebook |
| Deployment | Streamlit |
| Version Control | Git & GitHub |

---

# 📌 Current Progress

The repository currently includes:

- ✅ Project repository setup
- ✅ Project architecture
- ✅ Design documentation
- ✅ Dataset verification
- ✅ Dataset exploration
- ✅ Image preprocessing pipeline
- ✅ Image augmentation
- ✅ PyTorch Dataset creation
- ✅ DataLoader implementation

The remaining modules will be developed and integrated as the project progresses.

---

# 🧠 Deep Learning Approach

The project uses **Transfer Learning** with **MobileNetV2**, a lightweight convolutional neural network pretrained on the ImageNet dataset.

Instead of training a deep neural network from scratch, the pretrained feature extraction layers are reused, while the final classification layer is modified to classify the **38 PlantVillage classes**. This approach reduces training time, improves convergence, and achieves better performance, especially with limited computational resources.

---

# 📦 Installation

Clone the repository:

```bash
git clone https://github.com/aash0617/SeeIt-Crop-Disease-Classification.git
```

Move to the project directory:

```bash
cd SeeIt-Crop-Disease-Classification
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

# 📄 Note

The PlantVillage dataset is **not included** in this repository because of its large size. The dataset is stored locally and excluded using the `.gitignore` file.

---

# 👩‍💻 Author

**Aastha Bhalla**

B.Tech – Computer Science and Engineering (AI & Data Engineering)

Lovely Professional University

---

