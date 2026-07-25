import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset
import numpy as np
from pathlib import Path
from sklearn.model_selection import train_test_split

BASE_DIR = Path(__file__).resolve().parent
DATASET_DIR = BASE_DIR / "dataset"
GODOT_DIR = BASE_DIR / "godot.app"
GODOT_DIR.mkdir(exist_ok=True)

ONNX_OUTPUT = GODOT_DIR / "emotion_model.onnx"
WEIGHTS_OUTPUT = BASE_DIR / "emotion_model.pth"

# 1. Define PyTorch Neural Network Architecture
class EmotionClassifier(nn.Module):
    def __init__(self, input_dim=384, num_classes=6):
        super().__init__()
        self.network = nn.Sequential(
            nn.Linear(input_dim, 128),
            nn.BatchNorm1d(128),
            nn.GELU(),
            nn.Dropout(0.4),
            nn.Linear(128, 64),
            nn.BatchNorm1d(64),
            nn.GELU(),
            nn.Dropout(0.4),
            nn.Linear(64, num_classes)
        )

    def forward(self, x):
        return self.network(x)

if __name__ == "__main__":
    # 2. Load preprocessed features and labels
    X = np.load(DATASET_DIR / "train_x.npy")
    y = np.load(DATASET_DIR / "train_y.npy")

    num_classes = len(np.unique(y))
    print(f"Loaded dataset: {X.shape[0]} samples, {num_classes} emotion classes.")

    # 3. Train / Test Split (80% train, 20% test)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    train_ds = TensorDataset(torch.tensor(X_train, dtype=torch.float32), torch.tensor(y_train, dtype=torch.long))
    test_ds = TensorDataset(torch.tensor(X_test, dtype=torch.float32), torch.tensor(y_test, dtype=torch.long))

    train_loader = DataLoader(train_ds, batch_size=32, shuffle=True)
    test_loader = DataLoader(test_ds, batch_size=32, shuffle=False)

    # 4. Initialize Model, Loss Function, and Optimizer
    model = EmotionClassifier(input_dim=384, num_classes=num_classes)
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001, weight_decay=1e-4)
        # 5. Training Loop
    for epoch in range(20):
        model.train()  # Set model to training mode
        running_loss = 0.0
        correct_train = 0
        total_train = 0
        
        for batch_x, batch_y in train_loader:
            optimizer.zero_grad()
            
            # Forward pass
            noise = torch.randn_like(batch_x) * 0.02  # 2% random noise
            augmented_batch_x = batch_x + noise
            outputs = model(augmented_batch_x)
            loss = criterion(outputs, batch_y)
            
            # Backward pass & optimization
            loss.backward()
            optimizer.step()
            
            # Track Loss
            running_loss += loss.item()
            
            # Calculate Training Accuracy for this batch
            _, predicted = torch.max(outputs, 1)
            total_train += batch_y.size(0)
            correct_train += (predicted == batch_y).sum().item()
            
        avg_loss = running_loss / len(train_loader)
        train_accuracy = 100 * correct_train / total_train
    
    # --- Print Training Metrics for Each Epoch ---
    print(f"Epoch [{epoch+1:02d}/10] - Loss: {avg_loss:.4f} | Train Accuracy: {train_accuracy:.2f}%")

    # 6. Evaluation Phase
    print("\n📊 Evaluating Model Performance on Test Set...")
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for batch_x, batch_y in test_loader:
            outputs = model(batch_x)
            _, predicted = torch.max(outputs, 1)
            total += batch_y.size(0)
            correct += (predicted == batch_y).sum().item()

    accuracy = 100 * correct / total
    print(f"✅ Final Test Accuracy: {accuracy:.2f}%")

    # Save PyTorch weights
    torch.save(model.state_dict(), WEIGHTS_OUTPUT)

    # 7. Export Model to ONNX format for Godot
    print("\n📦 Exporting Model to ONNX format...")
    dummy_input = torch.randn(1, 384)
    torch.onnx.export(
        model,
        dummy_input,
        ONNX_OUTPUT,
        export_params=True,
        opset_version=14,
        do_constant_folding=True,
        input_names=['input_embedding'],
        output_names=['emotion_logits'],
        dynamic_axes={
            'input_embedding': {0: 'batch_size'},
            'emotion_logits': {0: 'batch_size'}
        }
    )
    print(f"🎉 Successfully exported ONNX model to: {ONNX_OUTPUT}")