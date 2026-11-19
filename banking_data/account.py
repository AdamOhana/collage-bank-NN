from dataclasses import dataclass
from enum import Enum


class OperationType(Enum):
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"
    SAVINGS = "savings"

@dataclass
class Account:
    owner: str
    _balance: float
    _savings: float
    _history: list

    def to_dict(self):
        return {
                "owner": self.owner,
                "balance": self._balance,
                "savings": self._savings,
                "history": self._history
        }


    def deposit(self, amount: float):
        self._balance += amount

    def withdraw(self, amount: float) -> bool:
        if amount > self._balance:
            return False
        self._balance -= amount
        return True

    def save(self, amount: float) -> bool:
        if amount > self._balance:
            return False
        self._balance -= amount
        self._savings += amount
        return True

    def update_history(self, action_type: str, amount: float, month: int):
        self._history.append({"type": action_type, "amount": amount, "month": month})

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value

    @property
    def history(self):
        return self._history

    @property
    def savings(self):
        return self._savings

    @savings.setter
    def savings(self, value):
        self._savings = value
