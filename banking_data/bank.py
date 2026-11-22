from banking_data.account import Account
from model.bank_brain import BankModel

OPERATIONS_PER_MONTH = 10
PERCENTAGE_PER_MONTH = 10
PERCENTAGE_TO_SAVE = 10
MIN_BALANCE = 50

class Bank:
    account_list: list[Account]
    month = 0
    operations = 0
    model = BankModel()

    def __init__(self, account_list: list[Account]):
        self.account_list = account_list

    def _validate_index(self, index: int) -> None:
        if index < 0 or index >= len(self.account_list):
            raise IndexError(f'Invalid account index: {index}')

    def show_accounts_dict(self) -> None:
        for i in range(len(self.account_list)):
            print(f"index: {i}\n", self.account_list[i].to_dict())

    def show_accounts_normal(self) -> None:
        for i, acc in enumerate(self.account_list):
            print(f"[{i}] {acc.get_data()}")

    def show_account_history(self, index: int) -> None:
        self._validate_index(index)
        acc = self.account_list[index]
        print(acc.get_history())

    def create_account(self, owner: str) -> None:
        acc = Account(owner)
        self.account_list.append(acc)
        print(f"New account {owner} created at index {len(self.account_list)}")


    def delete_account(self, index: int) -> None:
        self._validate_index(index)
        self.account_list.pop(index)

    def add_money(self, index: int, amount: float) -> None:
        self._validate_index(index)
        
        acc = self.account_list[index]
        acc.deposit(amount, self.month)
        self.inc_operations()

    def remove_money(self, index: int, amount: float) -> None:
        self._validate_index(index)
        
        acc = self.account_list[index]
        acc.withdraw(amount, self.month)
        self.inc_operations()

    def transfer_to_savings(self, index: int, amount: float) -> None:
        self._validate_index(index)

        acc = self.account_list[index]
        acc.save(amount, self.month)
        self.inc_operations()

    def send_money(self, from_index: int, to_index: int, amount: float) -> None:
        if from_index == to_index:
            raise IndexError(f'Cannot transfer money to self')
        self._validate_index(from_index)
        self._validate_index(to_index)

        acc1 = self.account_list[from_index]
        acc2 = self.account_list[to_index]
        acc1.withdraw(amount, self.month)
        acc2.deposit(amount, self.month)
        self.inc_operations()


    def inc_operations(self) -> None:
        self.operations += 1
        if self.operations % OPERATIONS_PER_MONTH == 0:
            self.month += 1
            self.trigger_savings()
            self.trigger_interest()
            self.model.update_epsilon()

    def trigger_savings(self) -> None:
        for account in self.account_list:
            action = self.model.pick_action(account)
            can_save = not account.under_minimum(MIN_BALANCE, PERCENTAGE_TO_SAVE)
            reward = 1 if (action == 1) == can_save else -1

            self.model.train(account, action, reward)

            if action == 1:
                cut = account.get_savings_cut(PERCENTAGE_TO_SAVE)
                if cut > 0:
                    account.save(cut, self.month)

            if self.month % 50 == 0:
                print(f"account [{account.owner}] chose {action} with can_save being {can_save}, reward: {reward}")

    def trigger_interest(self) -> None:
        for acc in self.account_list:
            acc.savings_interest(PERCENTAGE_PER_MONTH, self.month)
