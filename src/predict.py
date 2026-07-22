import torch
import torch.nn as nn
from torchvision import models
from pathlib import Path

from src.preprocess import preprocess_image
from src.class_names import CLASS_NAMES

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "mobilenet_plant_disease_new.pth"


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

class_names = CLASS_NAMES
num_classes = len(CLASS_NAMES)


def load_model():
    model = models.mobilenet_v2(weights=None)
    model.classifier[1] = nn.Linear(model.last_channel, num_classes)

    model.load_state_dict(
        torch.load(MODEL_PATH, map_location=device)
    )

    model.to(device)
    model.eval()

    return model


model = load_model()


def predict_image(image_path):

    image_tensor = preprocess_image(image_path).to(device)

    with torch.no_grad():

        outputs = model(image_tensor)

        probabilities = torch.softmax(outputs, dim=1)

    top_probs, top_indices = torch.topk(probabilities, 3)

    predictions = []

    for prob, idx in zip(top_probs[0], top_indices[0]):

        predictions.append({

            "class": class_names[idx.item()],

            "confidence": round(prob.item() * 100, 2)

        })

    predicted_class = predictions[0]["class"]

    confidence = predictions[0]["confidence"]

    return predicted_class, confidence, predictions




if __name__ == "__main__":

    image = BASE_DIR / "data" / "color" / "Apple___healthy"

    import os

    img = os.listdir(image)[0]

    img = image / img

    print(img)

    print(predict_image(img))        
