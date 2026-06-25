from sentence_transformers import SentenceTransformer
from quotes import QUOTES
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

texts = [q["text"] for q in QUOTES]

quote_embeddings = model.encode(texts)

# user = "I feel happy"
# user_embedding = model.encode(user)
# scores = cosine_similarity(
#     [user_embedding],
#     quote_embeddings
# )
# best = scores.argmax()
# quote = QUOTES[best]
# print(quote["text"])
# print(quote["mood"])

# while True:

#     user = input("You: ")

#     emb = model.encode(user)

#     scores = cosine_similarity(
#         [emb],
#         quote_embeddings
#     )

#     best = scores.argmax()

#     q = QUOTES[best]

#     print()
#     print(q["text"])
#     print("-", q["author"])
#     print("-", q["mood"])
#     print()

def get_embeddings(texts):
    return model.encode(texts)