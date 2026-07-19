# Reflection Piece

## Project Title

**SeeIt – Crop Leaf Disease Classification using Computer Vision and Deep Learning**

---

## Project Overview

During this internship, I developed **SeeIt**, a computer vision-based application that classifies crop leaf diseases using deep learning. The project uses the PlantVillage dataset and a MobileNetV2 model with transfer learning to identify diseases from leaf images. I also built a Streamlit web application that allows users to upload a leaf image and receive a disease prediction.

---

## What I Learned

This project significantly improved my understanding of deep learning and computer vision. Some of the key concepts I learned include:

- Image classification using Convolutional Neural Networks (CNNs)
- Transfer Learning with pretrained models
- Data preprocessing and augmentation
- Dataset splitting into training, validation, and test sets
- Model training and evaluation using PyTorch
- Saving and loading trained models
- Building an interactive Streamlit application
- Version control using Git and GitHub

Working on this project also strengthened my Python programming skills and helped me understand the complete machine learning workflow from data preparation to deployment.

---

## Challenges Faced

Throughout the project, I encountered several challenges.

Initially, I faced difficulty understanding the structure of the PlantVillage dataset and organizing it correctly. Managing a large image dataset and preprocessing it efficiently required careful planning.

Another challenge was understanding how transfer learning works and replacing the final classification layer of MobileNetV2 to support all 38 disease classes.

While deploying the application, I also had to resolve issues related to model loading, image preprocessing, and prediction consistency for user-uploaded images.

Finally, learning Git and GitHub workflows, handling commits, branches, merge conflicts, and repository management was another valuable learning experience.

---

## How I Solved These Challenges

I addressed these challenges by studying the official PyTorch documentation, experimenting with different preprocessing techniques, and testing the model multiple times.

Breaking the project into smaller tasks made development more manageable. I also learned to debug errors step by step rather than trying to solve everything at once.

Using notebooks for experimentation before integrating the code into the final application helped improve both accuracy and project organization.

---

## Project Outcome

The final model achieved:

- High validation accuracy during training.
- **97.68% accuracy on the test dataset.**
- Successful prediction of PlantVillage leaf images.
- A working Streamlit application capable of classifying crop leaf diseases.

The project demonstrates the practical application of computer vision and transfer learning in agriculture.

---

## Future Improvements

Although the project is functional, there are several enhancements that can be added in the future:

- Improve performance on real-world Google images collected under different lighting conditions.
- Train using a more diverse dataset containing natural backgrounds.
- Add Grad-CAM visualization to explain model predictions.
- Deploy the application on a cloud platform for public access.
- Expand the model to support additional crops and diseases.

---

## Personal Reflection

This project has been one of the most valuable learning experiences in my academic journey. It allowed me to apply theoretical concepts from artificial intelligence and deep learning to solve a real-world agricultural problem.

Beyond technical skills, I developed patience, problem-solving ability, and confidence in building an end-to-end machine learning application independently. I now have a much clearer understanding of the complete lifecycle of an AI project—from data collection and preprocessing to model development, evaluation, deployment, and documentation.

This internship has strengthened my interest in Artificial Intelligence and Computer Vision and has motivated me to continue exploring more advanced deep learning projects in the future.