from abc import ABC, abstractmethod
from banking_data.bank import Bank


class Command(ABC):
    label: str

    @abstractmethod
    def execute(self, bank: Bank) -> None:
        pass
