import torch
import torch.nn as nn
import torch.optim as optim
from banking_data.account import Account

MIN_BALANCE = 50

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

    def getState(self, account: Account) -> torch.Tensor:
        state = [1] if account.remainder(percentage=10) >= MIN_BALANCE else [0]
        return torch.tensor(state, dtype=torch.float).to(self.device)

    