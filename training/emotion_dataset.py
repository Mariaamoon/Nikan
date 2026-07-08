import torch
from torch.utils.data import Dataset
from sentence_transformers import SentenceTransformer

class emotiondataset(Dataset):
    def __init__(self,dataframe,embedder = None):
        self.text = dataframe["text"].tolist()
        self.labels = dataframe["label"].tolist()
        self.embedder = embedder or SentenceTransformer ("all-MiniLM-L6-v2")
        print("encoding...")
        self.embeddings = self.embedder.encode(
            self.texts,
            convert_to_tensor = True,
            show_progress_bar= True,
            batch_size= 64
        )
    def __le__(self):
        return len(self.labels)
    def __getitem__(self, index):
        return (
            self.embeddings[index],
            torch.tensor(self.labels[index], dtype=torch.long)
        )