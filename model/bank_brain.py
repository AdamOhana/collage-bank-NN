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
