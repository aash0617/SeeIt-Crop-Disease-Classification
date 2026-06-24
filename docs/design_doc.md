# Design Document: SeeIt - Crop Leaf Disease Classification

## 1. Project Overview

SeeIt is a Computer Vision based crop disease classification system developed using the PlantVillage dataset. The goal of the project is to help farmers identify crop diseases from leaf images using Deep Learning.

Users will be able to upload a crop leaf image and receive:

* Predicted disease class
* Confidence score
* Visual explanation using Grad-CAM

The project is developed under the I3 Vision Starter track.

---

## 2. Problem Statement

Crop diseases can significantly affect agricultural productivity. Early disease detection helps farmers take timely action and reduce crop loss.

The objective of this project is to build an image classification system that can automatically identify plant diseases from leaf images using transfer learning and deploy the model through an easy-to-use web application.

---

## 3. Dataset

### Dataset Name

PlantVillage Dataset

### Dataset Characteristics

* Approximately 54,000 images
* 38 disease and healthy classes
* Multiple crop species
* Three image representations:

  * Grayscale
  * Segmented
  * Color

### Example Classes

* Apple___Apple_scab
* Apple___Black_rot
* Tomato___Early_blight
* Tomato___healthy
* Potato___Late_blight

---

## 4. Proposed Approach

The same machine learning pipeline will be applied to all three image representations to compare their performance.

### Pipeline

Dataset Collection
→ Data Exploration
→ Train/Validation/Test Split
→ Image Preprocessing
→ MobileNetV2 Transfer Learning
→ Model Training
→ Model Evaluation
→ Grad-CAM Explainability
→ Streamlit Deployment
→ ONNX Export

---

## 5. Technical Stack

| Component               | Technology   |
| ----------------------- | ------------ |
| Programming Language    | Python       |
| Deep Learning Framework | PyTorch      |
| Model                   | MobileNetV2  |
| Image Processing        | Torchvision  |
| Evaluation              | Scikit-Learn |
| Visualization           | Matplotlib   |
| Explainability          | Grad-CAM     |
| Deployment              | Streamlit    |
| Export Format           | ONNX         |
| Version Control         | Git & GitHub |

---

## 6. Model Selection

MobileNetV2 has been selected because:

* Lightweight architecture
* Fast training and inference
* Suitable for deployment
* Good accuracy on image classification tasks
* Supports transfer learning

Transfer learning allows the model to leverage knowledge learned from millions of images while adapting to crop disease classification.

---

## 7. Evaluation Metrics

The model will be evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

Performance will be compared across grayscale, segmented, and color datasets.

---

## 8. Mini Extension

### Grad-CAM Explainability

Grad-CAM will be implemented to visualize the regions of the leaf that influenced the model's prediction.

Benefits:

* Improves transparency
* Helps understand model decisions
* Provides visual evidence of disease symptoms

---

## 9. Deployment Plan

A Streamlit web application will be developed where users can:

* Upload leaf images
* View disease predictions
* See confidence scores
* Visualize Grad-CAM heatmaps

---

## 10. Future Scope

Possible future enhancements include:

* YOLO-based disease detection
* Mobile deployment
* Edge deployment using ONNX
* Real-time disease monitoring
* Active learning pipeline
* Drift monitoring

---

## 11. Timeline

### Week 1

* Dataset exploration
* Class counting
* Image counting
* Dataset comparison

### Week 2

* MobileNetV2 training
* Validation
* Evaluation metrics

### Week 3

* Grad-CAM implementation
* Performance comparison

### Week 4

* Streamlit deployment
* ONNX export
* Documentation

### Week 5

* Final testing
* Reflection
* Resume bullets
* Showcase submission

---

## 12. Expected Outcome

The final system will classify crop leaf diseases from images and provide explainable predictions through a user-friendly web interface. The project will demonstrate practical applications of Computer Vision, Transfer Learning, Explainable AI, and Model Deployment in agriculture.
