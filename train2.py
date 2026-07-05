import pandas as pd


train_df = pd.read_csv(r"C:\Users\jam\Documents\nikan\dataset\training.csv")
val_df = pd.read_csv(r"C:\Users\jam\Documents\nikan\dataset\validation.csv")
test_df = pd.read_csv(r"C:\Users\jam\Documents\nikan\dataset\test.csv")
X_train = train_df["text"]
y_train = train_df["label"]

X_val = val_df["text"]
y_val = val_df["label"]

X_test = test_df["text"]
y_test = test_df["label"]

print(train_df.head())
print(train_df.columns)
print(train_df.shape)