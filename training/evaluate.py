import os
from pathlib import Path
import pandas as pd
import torch
import torch.nn as nn
from emotion_model import emotionclassifier
# ------------------------------------------------------------------
# 1. PATH RESOLUTION
# ------------------------------------------------------------------
# Get the directory where evaluate.py lives (D:\Nikan1\Nikan\training)
# .parent goes up one level to project root (D:\Nikan1\Nikan)
BASE_DIR = Path(__file__).resolve().parent.parent
DATASET_PATH = BASE_DIR / "dataset" / "test.csv"

# ------------------------------------------------------------------
# 3. SETUP DEVICE & MODEL INSTANTIATION
# ------------------------------------------------------------------
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Instantiate model without arguments
model = emotionclassifier().to(device)

# Load trained weights if available (Optional check)
weights_path = BASE_DIR / "training" / "model.pth"
if weights_path.exists():
    model.load_state_dict(torch.load(weights_path, map_location=device))
    print("Loaded pre-trained weights successfully.")

# ------------------------------------------------------------------
# 4. LOAD & PREPARE DATASET
# ------------------------------------------------------------------
print(f"Loading dataset from: {DATASET_PATH}")
test_df = pd.read_csv(DATASET_PATH)

# Assuming the label column is named 'label' (adjust if named differently)
if "label" in test_df.columns:
    X_raw = test_df.drop(columns=["label"]).values
    y_true = torch.tensor(test_df["label"].values, dtype=torch.long).to(device)
else:
    X_raw = test_df.values
    y_true = None

# Convert features to FloatTensor (shape: [batch_size, 384])
x_test = torch.tensor(X_raw, dtype=torch.float32).to(device)

# ------------------------------------------------------------------
# 5. MODEL EVALUATION / INFERENCE
# ------------------------------------------------------------------
model.eval()

with torch.no_grad():
    outputs = model(x_test)
    # Get predicted class indices
    predictions = torch.argmax(outputs, dim=1)

print("\n--- Evaluation Complete ---")
print(f"Evaluated {x_test.shape[0]} samples.")
print("Sample Predictions (First 5):", predictions[:5].tolist())

if y_true is not None:
    accuracy = (predictions == y_true).float().mean().item() * 100
    print(f"Accuracy: {accuracy:.2f}%")