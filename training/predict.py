import torch

from sentence_transformers import SentenceTransformer

from emotion_model import emotionclassifier

LABELS = {
    0: "sadness",
    1: "joy",
    2: "love",
    3: "anger",
    4: "fear",
    5: "surprise"
}

device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

embedder = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

model = emotionclassifier().to(device)

model.load_state_dict(
    torch.load(
        "models/emotion_classifier.pth",
        map_location=device
    )
)

model.eval()

while True:

    sentence = input("You: ")

    embedding = embedder.encode(
        sentence,
        convert_to_tensor=True
    ).unsqueeze(0).to(device)

    with torch.no_grad():

        prediction = model(
            embedding
        ).argmax(dim=1).item()

    print("Emotion:", LABELS[prediction])