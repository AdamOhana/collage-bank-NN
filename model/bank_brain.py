import random

import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from banking_data.account import Account

MIN_BALANCE = 50
BALANCE_SCALE = 1000

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
        self.epsilon = 0.9
        self.epsilon_decay = 0.05

    def get_state(self, account: Account) -> torch.Tensor:
        return torch.Tensor(account._balance/BALANCE_SCALE)

    def pick_action(self, account: Account) -> int:
        if random.random() < self.epsilon:
            self.epsilon *= self.epsilon_decay
            return random.randint(0, 1)
        with torch.no_grad():
            self.epsilon *= self.epsilon_decay
            return int(self.brain(self.get_state(account)).argmax())

    def train(self,account: Account ,action: int, reward: int) -> None:
        state = self.get_state(account).unsqueeze(0)  # (1, 1)
        prediction = self.brain(state)  # (1, 2)

        target = prediction.detach().clone()  # (1, 2), no gradient
        target[0, action] = reward  # only the taken action changes

        loss = F.mse_loss(prediction, target)

        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()
