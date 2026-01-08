import os
import json
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms, models
from torch.utils.data import DataLoader
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# Configuration
DATASET_DIR = "dataset"
IMG_SIZE = 224
BATCH_SIZE = 16
EPOCHS = 1
LEARNING_RATE = 0.001
DEVICE = torch.device("mps" if torch.backends.mps.is_available() else "cuda" if torch.cuda.is_available() else "cpu")

def train():
    if not os.path.exists(DATASET_DIR):
        print(f"Error: Dataset not found at {DATASET_DIR}")
        return

    print(f"Using device: {DEVICE}")

    # Data Augmentation & Normalization
    data_transforms = {
        'train': transforms.Compose([
            transforms.Resize((IMG_SIZE, IMG_SIZE)),
            transforms.RandomRotation(30),
            transforms.RandomHorizontalFlip(),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ]),
        'val': transforms.Compose([
            transforms.Resize((IMG_SIZE, IMG_SIZE)),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ]),
    }

    # Load Data
    # We need to manually split if the dataset folder doesn't have train/val subfolders.
    # The current dataset structure seems to be flat class folders.
    # So we need to do a random split.
    
    full_dataset = datasets.ImageFolder(root=DATASET_DIR)
    class_names = full_dataset.classes
    print(f"Classes: {class_names}")

    train_size = int(0.8 * len(full_dataset))
    val_size = len(full_dataset) - train_size
    train_dataset, val_dataset = torch.utils.data.random_split(full_dataset, [train_size, val_size])

    # Apply transforms
    # random_split doesn't allow separate transforms easily without a custom wrapper.
    # For simplicity, we'll use the 'train' transform for training subset and 'val' for validation is tricky.
    # We will wrap the subset to apply transforms.
    
    class TransformedSubset(torch.utils.data.Dataset):
        def __init__(self, subset, transform=None):
            self.subset = subset
            self.transform = transform
            
        def __getitem__(self, index):
            x, y = self.subset[index]
            if self.transform:
                x = self.transform(x)
            return x, y
        
        def __len__(self):
            return len(self.subset)

    train_set = TransformedSubset(train_dataset, transform=data_transforms['train'])
    val_set = TransformedSubset(val_dataset, transform=data_transforms['val'])

    dataloaders = {
        'train': DataLoader(train_set, batch_size=BATCH_SIZE, shuffle=True),
        'val': DataLoader(val_set, batch_size=BATCH_SIZE, shuffle=False)
    }

    # Save class indices
    class_indices = {name: idx for idx, name in enumerate(class_names)}
    with open("class_indices.json", "w") as f:
        json.dump(class_indices, f)
        
    print("Building Model (MobileNetV2)...")
    model = models.mobilenet_v2(weights=models.MobileNet_V2_Weights.DEFAULT)
    
    # Modify the last layer for our number of classes
    model.classifier[1] = nn.Linear(model.last_channel, len(class_names))
    
    model = model.to(DEVICE)

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE)

    print("Starting Training...")
    
    for epoch in range(EPOCHS):
        print(f"Epoch {epoch+1}/{EPOCHS}")
        print("-" * 10)

        for phase in ['train', 'val']:
            if phase == 'train':
                model.train()
            else:
                model.eval()

            running_loss = 0.0
            running_corrects = 0

            for inputs, labels in dataloaders[phase]:
                inputs = inputs.to(DEVICE)
                labels = labels.to(DEVICE)

                optimizer.zero_grad()

                with torch.set_grad_enabled(phase == 'train'):
                    outputs = model(inputs)
                    _, preds = torch.max(outputs, 1)
                    loss = criterion(outputs, labels)

                    if phase == 'train':
                        loss.backward()
                        optimizer.step()

                running_loss += loss.item() * inputs.size(0)
                running_corrects += torch.sum(preds == labels.data)

            epoch_loss = running_loss / len(dataloaders[phase].dataset)
            epoch_acc = running_corrects.float() / len(dataloaders[phase].dataset)

            print(f"{phase} Loss: {epoch_loss:.4f} Acc: {epoch_acc:.4f}")

    print("Saving model...")
    torch.save(model.state_dict(), "plant_disease_model.pt")
    print("Model saved as plant_disease_model.pt")

if __name__ == "__main__":
    train()
