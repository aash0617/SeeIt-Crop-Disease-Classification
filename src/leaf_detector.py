import torch
import torch.nn as nn
from torchvision import models
from src.preprocess import preprocess_image
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "leaf_detector.pth"

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

classes = ["leaf", "non_leaf"]


def load_leaf_detector():

    model = models.mobilenet_v2(weights=None)

    model.classifier[1] = nn.Linear(model.last_channel, 2)

    model.load_state_dict(torch.load(MODEL_PATH, map_location=device))

    model.to(device)

    model.eval()

    return model


leaf_model = load_leaf_detector()


def predict_leaf(image_path):

    image = preprocess_image(image_path).to(device)

    with torch.no_grad():

        output = leaf_model(image)

        probability = torch.softmax(output, dim=1)

        confidence, predicted = torch.max(probability, 1)

    return (
        classes[predicted.item()],
        round(confidence.item() * 100, 2)
    )