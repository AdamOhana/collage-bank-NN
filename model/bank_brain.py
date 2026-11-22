import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

class BankBrain(nn.Module):
    def __init__(self):
        super(BankBrain, self).__init__()
        self.fc1 = nn.Linear(1,2)

    def forward(self, x):
        x = self.fc1(x)
        return x

class BankModel:
    def __init__(self):
        self.brain = BankBrain()
        self.optimizer = optim.Adam(self.brain.parameters(), lr=0.001)
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    