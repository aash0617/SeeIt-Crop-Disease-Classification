# ADR-002: Selection of PlantVillage Dataset

## Status

Accepted

---

## Context

The project requires a labeled dataset containing healthy and diseased crop leaves for supervised image classification.

---

## Decision

The PlantVillage dataset was selected for training and evaluation.

The Color image dataset containing 38 disease classes was used.

---

## Rationale

The dataset provides:

- High-quality labeled images
- Multiple crop species
- Healthy and diseased leaf samples
- Balanced representation of disease classes
- Standard benchmark dataset for plant disease detection

---

## Consequences

### Advantages

- Reliable labels
- Easy integration with PyTorch
- Suitable for Transfer Learning
- Large number of images

### Trade-offs

- Images are captured under controlled conditions.
- Real-world images may contain complex backgrounds and lighting variations.