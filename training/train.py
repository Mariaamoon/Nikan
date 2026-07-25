import torch
import pandas as pd
from torch.utils.data import DataLoader
from emotion_dataset import emotiondataset
from emotion_model import emotionclassifier

train_df = pd.read_csv("D:/Nikan1/Nikan/dataset/training.csv")
val_df = pd.read_csv("D:/Nikan1/Nikan/dataset/validation.csv")

train_data = emotiondataset(train_df)
val_data = emotiondataset(val_df,embedder=train_data.embedder)

train_dataset = emotiondataset(train_df)
val_dataset = emotiondataset(
    val_df,
    embedder=train_dataset.embedder
)

train_loader = DataLoader(
    train_dataset,
    batch_size=64,
    shuffle=True
)

val_loader = DataLoader(
    val_dataset,
    batch_size=64
)

device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

model = emotionclassifier().to(device)

criterion = torch.nn.CrossEntropyLoss()

optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.001
)

epochs = 10

for epoch in range(epochs):

    model.train()

    total_loss = 0

    for embeddings, labels in train_loader:

        embeddings = embeddings.to(device)
        labels = labels.to(device)

        optimizer.zero_grad()

        outputs = model(embeddings)

        loss = criterion(outputs, labels)

        loss.backward()

        optimizer.step()

        total_loss += loss.item()

    print(
        f"Epoch {epoch+1}/{epochs}  Loss: {total_loss:.4f}"
    )
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "models"
MODEL_DIR.mkdir(exist_ok=True)
MODEL_PATH = MODEL_DIR / "emotion_classifier.pth"
torch.save(model.state_dict(), MODEL_PATH)
# torch.save(
#     model.state_dict(),
#     "modelss/emotion_classifier.pth"
# )

print("Model saved.")