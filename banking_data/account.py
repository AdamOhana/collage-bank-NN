from dataclasses import dataclass, field
from enum import StrEnum


class OperationType(StrEnum):
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"
    SAVINGS = "savings"
    INTEREST = "interest"

@dataclass
class Account:
    owner: str
    _balance: float = 0
    _savings: float = 0
    _history: list = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
                "owner": self.owner,
                "balance": self._balance,
                "savings": self._savings,
                "history": list(self._history)
        }

    def get_data(self) -> str:
        return  f"{self.owner:<10} balance: {self._balance:>8.2f}   savings: {self._savings:>8.2f}"

    def get_history(self) -> str:
        if not self._history:
            return "No history yet."
        lines = []
        for entry in self._history:
            lines.append(
                f"month {entry['month']:>2}: {entry['type']:<10} {entry['amount']:>8.2f}"
            )
        return "\n".join(lines)
    
    def _require_positive(self, amount: float, action: str) -> None:
        if amount <= 0:
            raise ValueError(f"{action} amount can't be non positive")

    def __post_init__(self) -> None:
        if not self.owner.strip():
            raise ValueError("Account name can't be empty")
        self.owner = self.owner.strip()

    def deposit(self, amount: float, month: int) -> None:
        self._require_positive(amount, OperationType.DEPOSIT)

        self._balance += amount
        self._update_history(OperationType.DEPOSIT, amount, month)

    def withdraw(self, amount: float, month: int) -> None:
        self._require_positive(amount, OperationType.WITHDRAWAL)
        if amount > self._balance:
            raise ValueError("Withdrawal amount can't be greater than your balance")

        self._balance -= amount
        self._update_history(OperationType.WITHDRAWAL, amount, month)

    def save(self, amount: float, month: int) -> None:
        self._require_positive(amount, OperationType.SAVINGS)
        if amount > self._balance:
            raise ValueError("Amount to transfer to savings can't be greater than your balance")

        self._balance -= amount
        self._savings += amount
        self._update_history(OperationType.SAVINGS, amount, month)

    def _update_history(self, action_type: str, amount: float, month: int):
        self._history.append({"type": action_type, "amount": amount, "month": month})

    def savings_interest(self, percentage: float, month: int) -> None:
        amount = self._savings * percentage / 100
        if amount <= 0:
            return
        self._savings += amount
        self._update_history(OperationType.INTEREST, amount, month)

