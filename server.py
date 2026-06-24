from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Server running"}

@app.get("/quote")
def quote():

    return {
        "text":"Believe in yourself.",
        "author":"Unknown"
    }

from pydantic import BaseModel


class UserMessage(BaseModel):
    text: str

#from train import model, quote_embeddings

@app.post("/recommend")
def recommend(msg: UserMessage):

    print(msg.text)

    return {
        "received": msg.text
    }