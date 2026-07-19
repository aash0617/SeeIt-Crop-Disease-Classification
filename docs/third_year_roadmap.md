# Third Year Roadmap

## Project: SeeIt – Crop Leaf Disease Classification

### Objective

The primary goal for the third year is to transform **SeeIt** from a prototype image classification system into a complete AI-powered crop disease diagnosis platform that can be used in real-world agricultural environments. The focus will be on improving model accuracy, enhancing user experience, supporting real-world images, and deploying the application on mobile and edge devices.

---

# Phase 1: Improve Leaf Detection

### Current Status

The current application works best when a clear image of a single leaf is uploaded. It expects the leaf to be clearly visible, which may not always be the case in real-world scenarios.

### Future Improvements

- Improve the leaf detection model to accurately identify leaves from complex backgrounds.
- Support detection of multiple leaves within a single image.
- Automatically crop the detected leaf before sending it for disease prediction.
- Increase robustness against varying lighting conditions and camera angles.

### Expected Outcome

A more reliable and automated prediction pipeline that requires minimal user effort and performs well in natural farming environments.

---

# Phase 2: Build Better Deep Learning Models

### Current Model

- MobileNetV2 (Transfer Learning)

### Future Improvements

To improve prediction performance, I plan to compare MobileNetV2 with more advanced deep learning architectures, including:

- EfficientNet
- ResNet50
- ConvNeXt
- Vision Transformer (ViT)

Each model will be evaluated using accuracy, precision, recall, F1-score, inference speed, and model size.

### Expected Outcome

Selecting the best-performing model that provides higher accuracy while maintaining efficient inference suitable for deployment.

---

# Phase 3: Train on Real-World Dataset

### Current Dataset

The current model is trained on the PlantVillage dataset, where images are captured under controlled laboratory conditions.

### Future Improvements

Collect and integrate real-world crop images from:

- Agricultural fields
- Mobile phone cameras
- Different weather conditions
- Various lighting environments
- Multiple crop growth stages

This will make the model more robust and capable of handling practical scenarios.

### Expected Outcome

Improved generalization and higher prediction accuracy on real-world images.

---

# Phase 4: Explainable AI (Grad-CAM)

### Future Improvements

Integrate Grad-CAM (Gradient-weighted Class Activation Mapping) to visualize the regions of the leaf that influenced the model's prediction.

The system will:

- Highlight infected areas.
- Explain why a disease was predicted.
- Increase transparency and user trust.

### Expected Outcome

An interpretable AI system that provides both predictions and visual explanations.

---

# Phase 5: Mobile Application Development

### Future Improvements

Develop a cross-platform mobile application that allows farmers to:

- Capture leaf images directly using a smartphone.
- Receive instant disease predictions.
- View disease descriptions.
- Access treatment recommendations.
- Save previous prediction history.

### Technologies

- Flutter
- PyTorch Mobile / TensorFlow Lite
- Firebase

### Expected Outcome

A user-friendly mobile application that makes disease diagnosis accessible to farmers anywhere.

---

# Phase 6: Edge Deployment

### Future Improvements

Optimize the trained model for deployment on edge devices such as:

- Raspberry Pi
- NVIDIA Jetson Nano
- Android devices

The optimized model will provide:

- Offline predictions
- Faster inference
- Lower latency
- Reduced internet dependency

### Expected Outcome

A lightweight AI solution suitable for remote agricultural regions with limited internet connectivity.

---

# Phase 7: Cloud-Based Smart Farming Platform

### Future Improvements

Extend the application by integrating cloud technologies to provide:

- Secure farmer authentication
- Prediction history
- Cloud database storage
- Disease analytics dashboard
- Crop monitoring reports

### Expected Outcome

A centralized platform capable of supporting multiple users while maintaining historical prediction records and analytics.

---

# Phase 8: Expand Disease Coverage

### Current Scope

The current model supports classification of 38 PlantVillage disease classes.

### Future Improvements

Expand the system to include:

- Additional crop species
- More plant diseases
- Pest identification
- Nutrient deficiency detection
- Early disease warning system

### Expected Outcome

A comprehensive AI-based crop health monitoring solution capable of assisting farmers throughout the crop lifecycle.

---

# Long-Term Vision

By the end of the third year, I aim to transform **SeeIt** into a complete AI-powered agricultural assistant capable of real-time disease detection, explainable predictions, mobile accessibility, cloud integration, and edge deployment.

The project will evolve from an academic prototype into a practical solution that can support farmers in early disease detection, reduce crop losses, and contribute to smarter and more sustainable agriculture.