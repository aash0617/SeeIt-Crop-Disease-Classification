# Mock Interview Questions

## Q1. Why did you choose MobileNetV2?

MobileNetV2 is a lightweight convolutional neural network designed for efficient image classification. It provides high accuracy while requiring fewer parameters and lower computational resources, making it suitable for deployment on mobile and edge devices.

---

## Q2. Why did you use Transfer Learning?

Training a deep neural network from scratch requires a very large dataset and significant computational resources. Transfer Learning allows us to use a pretrained model that has already learned useful image features, reducing training time and improving accuracy.

---

## Q3. Why did you choose the PlantVillage dataset?

The PlantVillage dataset is a publicly available benchmark dataset for crop disease classification. It contains more than 54,000 labeled images across 38 disease categories, making it ideal for training and evaluating image classification models.

---

## Q4. Why did you use PyTorch?

PyTorch provides a flexible and easy-to-use deep learning framework with dynamic computation graphs, making model development, debugging, and experimentation much simpler.

---

## Q5. How can you improve the accuracy of this project?

Possible improvements include:

- Collecting real-world agricultural images.
- Training on larger and more diverse datasets.
- Comparing multiple deep learning architectures such as EfficientNet and Vision Transformers.
- Fine-tuning more layers of the pretrained model.
- Applying advanced data augmentation techniques.

---

## Q6. What preprocessing steps were applied?

The images were:

- Resized to 224×224 pixels.
- Converted into tensors.
- Normalized using ImageNet mean and standard deviation.
- Augmented using random rotation and horizontal flipping during training.

---

## Q7. What was your final model performance?

The final MobileNetV2 model achieved approximately **97.68% test accuracy** on the PlantVillage dataset.

---

## Q8. What are the future improvements for this project?

Future work includes:

- Better leaf detection.
- Grad-CAM based explainability.
- Mobile application development.
- Edge device deployment.
- Cloud integration.
- Support for additional crops and diseases.