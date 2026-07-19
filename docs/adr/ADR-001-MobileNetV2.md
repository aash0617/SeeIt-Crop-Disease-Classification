# ADR-001: Selection of MobileNetV2 for Disease Classification

## Status

Accepted

---

## Context

The project aims to classify crop leaf diseases using deep learning. The model should provide high accuracy while remaining lightweight and suitable for deployment on systems with limited computational resources.

---

## Decision

MobileNetV2 was selected as the base deep learning model.

The model uses Transfer Learning with pretrained ImageNet weights. The final classification layer was replaced with a fully connected layer containing 38 output classes corresponding to the PlantVillage dataset.

---

## Rationale

The following reasons influenced this decision:

- Lightweight CNN architecture
- Faster training compared to larger networks
- Lower computational requirements
- Good classification accuracy
- Easy deployment using Streamlit
- Widely used for image classification tasks

---

## Consequences

### Advantages

- Reduced training time
- High prediction accuracy
- Smaller model size
- Faster inference
- Suitable for real-time applications

### Trade-offs

- May perform slightly below larger models such as ResNet50 on highly complex datasets.