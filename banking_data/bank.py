from banking_data.account import Account


OPERATIONS_PER_MONTH = 10
PERCENTAGE_PER_MONTH = 10

class Bank:
    account_list: list[Account]
    month = 0
    operations = 0

    def __init__(self, account_list: list[Account]):
        self.account_list = account_list

    def _validate_index(self, index: int) -> None:
        if index < 0 or index >= len(self.account_list):
            raise IndexError(f'Invalid account index: {index}')

    def show_accounts(self) -> None:
        for i in range(len(self.account_list)):
            print(f"index: {i}\n", self.account_list[i].to_dict(), sep="")

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

    def trigger_savings(self):
        pass

    def trigger_interest(self) -> None:
        for acc in self.account_list:
            acc.savings_interest(PERCENTAGE_PER_MONTH, self.month)
