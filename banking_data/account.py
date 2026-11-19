from dataclasses import dataclass


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
