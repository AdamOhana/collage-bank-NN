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

class DepositMoney(Command):
    label: str = 'Deposit Money'
    def execute(self, bank: Bank) -> None:
        index = int(input('Account index: '))
        amount = float(input('Amount: '))
        bank.add_money(index, amount)

class DeleteAccount(Command):
    label: str = 'Delete Account'
    def execute(self, bank: Bank) -> None:
        index = int(input('Account index: '))
        bank.delete_account(index)

class WithdrawMoney(Command):
    label: str = 'Withdraw Money'
    def execute(self, bank: Bank) -> None:
        index = int(input('Account index: '))
        amount = float(input('Amount: '))
        bank.remove_money(index, amount)

class TransferToSavings(Command):
    label: str = 'Transfer To Savings'
    def execute(self, bank: Bank) -> None:
        index = int(input('Account index: '))
        amount = float(input('Amount: '))
        bank.transfer_to_savings(index, amount)

class SendMoney(Command):
    label: str = 'Send Money'
    def execute(self, bank: Bank) -> None:
        from_index = int(input('From account index: '))
        to_index = int(input('To account index: '))
        amount = float(input('Amount: '))
        bank.send_money(from_index, to_index, amount)
