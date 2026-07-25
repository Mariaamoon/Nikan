import pandas as pd
import numpy as np
import torch
from pathlib import Path
from sentence_transformers import SentenceTransformer

BASE_DIR = Path(__file__).resolve().parent
DATASET_PATH = BASE_DIR / "dataset" / "training.csv"  # Adjust filename to match your CSV
OUTPUT_DIR = BASE_DIR / "dataset"

# 1. Load Model for Sentence Embeddings
print("Loading embedding model...")
model = SentenceTransformer('all-MiniLM-L6-v2')

# 2. Load Kaggle CSV
print(f"Loading {DATASET_PATH}...")
df = pd.read_csv(DATASET_PATH)
print(df.head())
# Assume columns are 'text' and 'label' (change if yours are named 'sentence', 'emotion', etc.)
texts = df['text'].tolist()
labels = df['label'].values  # Integer values 0..5 or categorical

# Encode labels if string categories
if df['label'].dtype == object:
    label_mapping = {val: i for i, val in enumerate(df['label'].unique())}
    labels = np.array([label_mapping[val] for val in df['label']])
    print("Label Mapping:", label_mapping)

# 3. Generate 384-dimensional embeddings for Kaggle text
print(f"Generating embeddings for {len(texts)} samples...")
embeddings = model.encode(texts, show_progress_bar=True)

# 4. Save arrays for fast training
np.save(OUTPUT_DIR / "train_x.npy", embeddings)
np.save(OUTPUT_DIR / "train_y.npy", labels)

print("✅ Kaggle dataset prepared and saved!")