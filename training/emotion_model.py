import torch.nn as nn
class emotionclassifier(nn.module):
    def __init__(self):
        super().__init__()
        self.network=nn.Sequential(
            nn.Linear(384,256),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(256,128),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(128,6)
        )
    def forward(self , x):
        return self.network(x)