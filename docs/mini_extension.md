# Mini Extension

## Title
Leaf Detection Before Disease Classification

## Description

The original project classified diseases directly from uploaded images. As a mini extension, a leaf detection module was added.

The system now performs the following steps:

1. Detect the leaf in the uploaded image.
2. Crop the detected leaf region.
3. Preprocess the cropped image.
4. Classify the disease using the trained MobileNetV2 model.

## Benefits

- Better input quality for the classifier.
- Reduces background noise.
- Provides a modular prediction pipeline.
- Creates a foundation for future real-world deployment.

## Files

- src/leaf_detector.py
- models/leaf_detector.pth
- notebooks/05_leaf_detector.ipynb