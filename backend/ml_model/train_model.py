import os
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader
from torchvision import datasets, transforms, models
from torch.optim import Adam
from PIL import Image

# Device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# Directories
DATA_DIR = "data"
TRAIN_DIR = os.path.join(DATA_DIR, "training_set/training_set")
TEST_DIR = os.path.join(DATA_DIR, "test_set/test_set")
MODEL_DIR = "ml_model"
MODEL_PATH = os.path.join(MODEL_DIR, "cat_dog_model.pth")
os.makedirs(MODEL_DIR, exist_ok=True)


# Image transforms
transform = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.ToTensor(),
    # Normalization for pretrained ResNet
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
])

# ----------------------------
# Load datasets
# For training purposes only
# ----------------------------
# train_data = datasets.ImageFolder(root=TRAIN_DIR, transform=transform)
# train_loader = DataLoader(train_data, batch_size=16, shuffle=True)

# test_data = datasets.ImageFolder(root=TEST_DIR, transform=transform)
# test_loader = DataLoader(test_data, batch_size=16, shuffle=False)


# Model setup
def build_model():
    """Load pretrained ResNet50 and modify final layer for 2 classes."""
    model = models.mobilenet_v2(weights=models.MobileNet_V2_Weights.IMAGENET1K_V1)
    num_features = model.classifier[1].in_features  # last linear layer
    model.classifier[1] = nn.Linear(num_features, 2)  # 2 classes: cat, dog
    return model

def load_model(model_path=MODEL_PATH, device=device):
    """Load trained model from disk (if exists)."""
    model = build_model()
    if os.path.exists(model_path):
        model.load_state_dict(torch.load(model_path, map_location=device)) # Load model to specified device
        print(f"Loaded model from {model_path}")
    model.to(device)
    model.eval()
    return model

model = load_model()

#----------------------------
# Training (commented out for now)
#----------------------------
# model = build_model().to(device)
# criterion = nn.CrossEntropyLoss()
# optimizer = Adam(model.parameters(), lr=1e-4)

# epochs = 1
# for epoch in range(epochs):
#     model.train()
#     total_loss = 0
#     for imgs, labels in train_loader:
#         imgs, labels = imgs.to(device), labels.to(device)
#         optimizer.zero_grad()
#         outputs = model(imgs)
#         loss = criterion(outputs, labels)
#         loss.backward()
#         optimizer.step()
#         total_loss += loss.item()
#     print(f"Epoch [{epoch+1}/{epochs}], Loss: {total_loss/len(train_loader):.4f}")

# # Evaluate model
# model.eval()
# correct = 0
# total = 0
# with torch.no_grad():
#     for imgs, labels in test_loader:
#         imgs, labels = imgs.to(device), labels.to(device)
#         outputs = model(imgs)
#         _, preds = outputs.max(1)
#         total += labels.size(0)
#         correct += (preds == labels).sum().item()

# accuracy = correct / total
# print(f"Test Accuracy: {accuracy*100:.2f}%")

# torch.save(model.state_dict(), MODEL_PATH)
# print(f"Model saved at {MODEL_PATH}")


# def predict_image(image_path_or_file):
#     """
#     Predict whether an image is a cat or dog.
#     """
#     model.eval()
#     try:
#         from PIL import Image
#         if isinstance(image_path_or_file, str):
#             img = Image.open(image_path_or_file).convert("RGB")
#         else:
#             img = Image.open(image_path_or_file.file).convert("RGB")

#         img = transform(img).unsqueeze(0).to(device)

#         with torch.no_grad():
#             outputs = model(img)
#             _, pred = outputs.max(1) # Get the index of the max log-probability

#         labels = ["cat", "dog"]
#         return labels[pred.item()]
#     except Exception as e:
#         print(f"Error predicting image: {e}")
#         return None


# For training purposes only
# if __name__ == "__main__":
#     sample_image = os.path.join(TEST_DIR, "cats/cat.4001.jpg")
#     prediction = predict_image(sample_image)
#     print(f"Predicted class for {sample_image}: {prediction}")



def predict_image(image_path_or_file):
    """
    Predict probabilities for cat, dog, and other.
    Returns: dict like {"cat": 0.9, "dog": 0.05, "other": 0.05}
    """
    model.eval()
    try:
        from PIL import Image

        # Load image (works for Django InMemoryUploadedFile or file path)
        if isinstance(image_path_or_file, str):
            img = Image.open(image_path_or_file).convert("RGB")
        else:
            img = Image.open(image_path_or_file.file).convert("RGB")

        # Preprocess
        img = transform(img).unsqueeze(0).to(device)

        with torch.no_grad():
            outputs = model(img)                  # raw logits
            probs = F.softmax(outputs, dim=1)[0]  # convert to probabilities

        # Get class probabilities
        cat_prob = probs[0].item()
        dog_prob = probs[1].item()

        # Estimate "other" as residual (useful when neither cat nor dog is confident)
        other_prob = max(0.0, 1.0 - (cat_prob + dog_prob))

        result = {
            "cat": round(cat_prob, 4),
            "dog": round(dog_prob, 4),
            "other": round(other_prob, 4)
        }

        return result

    except Exception as e:
        print(f"Error predicting image: {e}")
        return {"cat": 0, "dog": 0, "other": 1}
