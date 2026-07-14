import os
import random
import shutil
from pathlib import Path

# Change this path if your project is somewhere else
BASE_DIR = Path(r"C:\Users\bhall\OneDrive\Desktop\project\leaf_detector_dataset")

random.seed(42)

for cls in ["leaf", "non_leaf"]:

    images = list((BASE_DIR / cls).glob("*"))

    random.shuffle(images)

    total = len(images)

    train_size = int(0.70 * total)
    val_size = int(0.15 * total)

    train = images[:train_size]
    val = images[train_size:train_size + val_size]
    test = images[train_size + val_size:]

    for split_name, split_images in zip(
        ["train", "val", "test"],
        [train, val, test]
    ):

        split_folder = BASE_DIR / split_name / cls
        split_folder.mkdir(parents=True, exist_ok=True)

        for img in split_images:
            shutil.copy(img, split_folder / img.name)

print("✅ Dataset successfully split!")