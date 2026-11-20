from abc import ABC, abstractmethod
from banking_data.bank import Bank


class Command(ABC):
    label: str

    @abstractmethod
    def execute(self, bank: Bank) -> None:
        pass

class CreateAccount(Command):
    label: str = 'Create Account'
    def execute(self, bank: Bank) -> None:
        bank.create_account()

class ShowAccounts(Command):
    label: str = 'Show Accounts'
    def execute(self, bank: Bank) -> None:
        bank.show_accounts()

