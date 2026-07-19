# ADR-003: Selection of Streamlit for Deployment

## Status

Accepted

---

## Context

The trained deep learning model requires a user-friendly interface that allows users to upload leaf images and obtain disease predictions.

---

## Decision

Streamlit was selected as the deployment framework.

---

## Rationale

Streamlit provides:

- Simple Python-based deployment
- Fast development
- Interactive user interface
- Easy integration with PyTorch models
- File upload support
- Minimal frontend development

---

## Consequences

### Advantages

- Easy to build and maintain
- Quick deployment
- User-friendly interface
- Suitable for project demonstrations

### Trade-offs

- Limited frontend customization compared to full-stack web frameworks.