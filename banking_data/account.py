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

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self.balance = value

    @property
    def history(self):
        return self._history

    @property
    def savings(self):
        return self._savings

    @savings.setter
    def savings(self, value):
        self._savings = value
