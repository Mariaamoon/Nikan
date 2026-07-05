import random
import pandas as pd
from quotes import QUOTES
from tqdm import tqdm
LABEL_TO_EMOTION = {
    0: "sadness",
    1: "joy",
    2: "love",
    3: "anger",
    4: "fear",
    5: "surprise",
}
EMOTION_TO_MOOD = {
    "sadness": [
        "compassion",
        "motivational",
        "reflecting",
        "wisdom",
        "loss"
    ],

    "fear": [
        "motivational",
        "wisdom",
        "reflecting"
    ],

    "anger": [
        "compassion",
        "wisdom",
        "reflecting"
    ],

    "joy": [
        "joy",
        "love",
        "humorous"
    ],

    "love": [
        "love",
        "compassion"
    ],

    "surprise": [
        "reflecting",
        "wisdom"
    ]
}
quotes_by_mood = {}

for quote in QUOTES:

    mood = quote["mood"]

    quotes_by_mood.setdefault(mood, []).append(quote)

train_df = pd.read_csv(r"C:\Users\jam\Documents\nikan\dataset\training.csv")
val_df = pd.read_csv(r"C:\Users\jam\Documents\nikan\dataset\validation.csv")
test_df = pd.read_csv(r"C:\Users\jam\Documents\nikan\dataset\test.csv")

emotion_df = pd.concat(
    [train_df, val_df, test_df],
    ignore_index=True
)

print(f"Loaded {len(emotion_df)} emotion sentences.")

# -----------------------------
# Group quotes by mood
# -----------------------------

quotes_by_mood = {}

for quote in QUOTES:
    mood = quote["mood"]
    quotes_by_mood.setdefault(mood, []).append(quote["text"])

all_moods = list(quotes_by_mood.keys())

# -----------------------------
# Precompute positive/negative pools
# -----------------------------

emotion_quote_pool = {}

for emotion, positive_moods in EMOTION_TO_MOOD.items():

    positive_quotes = []

    for mood in positive_moods:
        positive_quotes.extend(quotes_by_mood.get(mood, []))

    negative_quotes = []

    for mood in all_moods:
        if mood not in positive_moods:
            negative_quotes.extend(quotes_by_mood[mood])

    emotion_quote_pool[emotion] = {
        "positive": positive_quotes,
        "negative": negative_quotes
    }

# -----------------------------
# Generate training pairs
# -----------------------------

pairs = []

records = emotion_df.to_dict("records")

for row in tqdm(records, desc="Generating pairs"):

    sentence = row["text"]

    emotion = LABEL_TO_EMOTION[row["label"]]

    pools = emotion_quote_pool[emotion]

    # Create multiple positives
    for quote in random.sample(
        pools["positive"],
        min(3, len(pools["positive"]))
    ):

        pairs.append({
            "sentence": sentence,
            "quote": quote,
            "label": 1
        })

    # Create multiple negatives
    for quote in random.sample(
        pools["negative"],
        min(3, len(pools["negative"]))
    ):

        pairs.append({
            "sentence": sentence,
            "quote": quote,
            "label": 0
        })

# -----------------------------
# Save
# -----------------------------

pairs_df = pd.DataFrame(pairs)

pairs_df.to_csv(
    "dataset/training_pairs.csv",
    index=False
)

print("\nDone!")
print("Total training pairs:", len(pairs_df))
print(pairs_df.head())