from pathlib import Path

from PIL import Image
from torchvision import transforms
from torchvision.datasets import ImageFolder

# Same preprocessing used during training
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])


def preprocess_image(image_path):
    image = Image.open(image_path).convert("RGB")
    image = transform(image)
    return image.unsqueeze(0)


def get_class_names(data_dir):
    data_dir = Path(data_dir)
    dataset = ImageFolder(root=data_dir)
    return dataset.classes