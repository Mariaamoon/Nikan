from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"status": "ready"}

@app.get("/quote")
def quote():

    return {
        "text":"Believe in yourself.",
        "author":"Unknown"
    }

from pydantic import BaseModel
from train import get_embeddings,model
from quotes import QUOTES
from sklearn.metrics.pairwise import cosine_similarity

texts = [q["text"] for q in QUOTES]
quote_embeddings = get_embeddings(texts)

class UserMessage(BaseModel):
    text: str

@app.post("/recommend")
def recommend(msg: UserMessage):

    print(msg.text)

    emb = model.encode(msg.text)

    scores = cosine_similarity(
        [emb],
        quote_embeddings
    )

    best = scores.argmax()

    return QUOTES[best]

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000
    )