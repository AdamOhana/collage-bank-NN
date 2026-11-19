import dataclasses


@dataclasses
class Account:
    owner: str
    balance: float
    savings: float
    history: dict
