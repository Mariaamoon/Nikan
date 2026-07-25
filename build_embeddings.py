import os
import numpy as np
from pathlib import Path
from sentence_transformers import SentenceTransformer
from quotes import QUOTES # Loads your quote dictionary

# 1. Anchor paths relative to this file so cloud deployment won't break
BASE_DIR = Path(__file__).resolve().parent
DATASET_DIR = BASE_DIR / "dataset"
DATASET_DIR.mkdir(exist_ok=True)  # Create folder if it doesn't exist

OUTPUT_FILE = DATASET_DIR / "quote_embeddings.npy"

# 2. Load lightweight sentence transformer
print("Loading sentence transformer model...")
model = SentenceTransformer('all-MiniLM-L6-v2')

# 3. Extract quote texts from dictionary
# Assumes structure: {"q1": "Text...", "q2": "Text..."} or similar
texts = [q["text"] for q in QUOTES]

print(f"Generating embeddings for {len(texts)} quotes...")
embeddings = model.encode(texts, show_progress_bar=True)

# 4. Save vectors to numpy array
np.save(OUTPUT_FILE, embeddings)
print(f"✅ Embeddings successfully saved to {OUTPUT_FILE}!")