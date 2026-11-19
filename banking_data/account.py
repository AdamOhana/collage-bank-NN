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
