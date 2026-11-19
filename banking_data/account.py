from dataclasses import dataclass
from enum import StrEnum


class OperationType(StrEnum):
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"
    SAVINGS = "savings"
    INTEREST = "interest"

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


    def deposit(self, amount: float, month: int) -> None:
        self._balance += amount
        self.update_history(OperationType.DEPOSIT, amount, month)

    def withdraw(self, amount: float, month: int) -> bool:
        if amount > self._balance:
            return False
        self._balance -= amount
        self.update_history(OperationType.WITHDRAWAL, amount, month)
        return True

    def save(self, amount: float, month: int) -> bool:
        if amount > self._balance:
            return False
        self._balance -= amount
        self._savings += amount
        self.update_history(OperationType.SAVINGS, amount, month)
        return True

    def update_history(self, action_type: str, amount: float, month: int):
        self._history.append({"type": action_type, "amount": amount, "month": month})

    def savings_interest(self, percentage: float, month: int) -> None:
        amount = self._savings * percentage / 100
        if amount <= 0:
            return
        self._savings += amount
        self.update_history(OperationType.INTEREST, amount, month)

