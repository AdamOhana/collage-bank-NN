from dataclasses import dataclass


@dataclass
class Account:
    owner: str
    balance: float
    savings: float
    history: dict

    def to_dict(self):
        return {
                "owner": self.owner,
                "balance": self.balance,
                "savings": self.savings,
                "history": self.history
        }
