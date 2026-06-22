from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Server running"}

@app.get("/quote")
def quote():
    return {
        "text": "Believe in yourself.",
        "author": "Unknown"
    }