import json
import numpy as np
from pathlib import Path
from quotes import QUOTES

BASE_DIR = Path(__file__).resolve().parent
EMBEDDINGS_PATH = BASE_DIR / "dataset" / "quote_embeddings.npy"
OUTPUT_JSON = BASE_DIR / "godot.app" / "quotes_data.json"  # Saves into Godot folder

# 1. Load pre-computed numpy vectors
embeddings = np.load(EMBEDDINGS_PATH)
texts = [q["text"] for q in QUOTES]

# 2. Structure data for Godot
data = []
for i, quote_text in enumerate(texts):
    data.append({
        "id": i,
        "text": quote_text,
        "embedding": embeddings[i].tolist()  # Convert numpy array to standard JSON list
    })

# 3. Save as JSON
with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ Exported {len(data)} quotes with embeddings to {OUTPUT_JSON}!")