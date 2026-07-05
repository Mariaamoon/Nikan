import pandas as pd

df = pd.read_csv("dataset/training_pairs.csv")

df = df[df["label"] == 1]

df.to_csv("dataset/positive_pairs.csv", index=False)

print(len(df))

print("Unique pairs:", len(df.drop_duplicates()))