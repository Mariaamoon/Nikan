import random
import numpy as np
from pathlib import Path
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from quotes import QUOTES

BASE_DIR = Path(__file__).resolve().parent
EMBEDDINGS_PATH = BASE_DIR / "dataset" / "quote_embeddings.npy"

# Load model and pre-computed embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')

if EMBEDDINGS_PATH.exists():
    quote_embeddings = np.load(EMBEDDINGS_PATH)
else:
    raise FileNotFoundError("Run build_embeddings.py first to create quote_embeddings.npy!")

# Get quote list in matching order
texts = [q["text"] for q in QUOTES]

# Friendly conversation templates
TEMPLATES = [
    "I hear you. When things feel that way, I find comfort in this thought:",
    "Thank you for opening up to me. Here is a quote that might offer some perspective:",
    "I completely understand where you're coming from. Take a moment with this:",
    "That is totally valid. Keep this reflection in mind today:"
]

def get_recommendation(user_input: str, user_name: str = "Friend") -> str:
    # 1. Convert user's input message into vector
    user_vec = model.encode([user_input])
    
    # 2. Find closest quote via Cosine Similarity
    similarities = cosine_similarity(user_vec, quote_embeddings)[0]
    best_idx = np.argmax(similarities)
    matched_quote = texts[best_idx]
    
    # 3. Build empathetic conversational output
    intro = random.choice(TEMPLATES)
    return f"Hey {user_name}! {intro}\n\n👉 \"{matched_quote}\""