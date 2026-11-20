from banking_data.account import Account


OPERATIONS_PER_MONTH = 10
PERCENTAGE_PER_MONTH = 10

class Bank:
    account_list: list[Account]
    top: int
    month = 0
    operations = 0

    def __init__(self, account_list: list[Account]):
        self.account_list = account_list
        self.top = len(account_list)

    def show_accounts(self) -> None:
        for i in range(self.top):
            print(f"index: {i}\n", self.account_list[i].to_dict(), sep="")

    def create_account(self, owner: str) -> None:
        acc = Account(owner)
        self.account_list.append(acc)
        print(f"New account {owner} created at index {self.top}")
        self.top += 1


    def delete_account(self, index: int) -> bool:
        if (0 <= index < self.top):
            self.account_list.pop(index)
            self.top -= 1
            return True
        return False

    def add_money(self, index: int, amount: float) -> bool:
        if not (0 <= index < self.top):
            return False
        
        acc = self.account_list[index]

        acc.deposit(amount, self.month)
        self.inc_operations()
        return True

    def remove_money(self, index: int, amount: float) -> bool:
        if not (0 <= index < self.top):
            return False
        
        acc = self.account_list[index]

        if acc.withdraw(amount, self.month):
            self.inc_operations()
            return True
        return False

    def transfer_to_savings(self, index: int, amount: float) -> bool:
        if not (0 <= index < self.top):
            return False
        
        acc = self.account_list[index]

        if acc.save(amount, self.month):
            self.inc_operations()
            return True
        return False

    def send_money(self, from_index: int, to_index: int, amount: float) -> bool:
        if not (0 <= from_index < self.top) or not (0 <= to_index < self.top):
            return False

        acc1 = self.account_list[from_index]
        acc2 = self.account_list[to_index]

        if acc1.withdraw(amount, self.month):
            acc2.deposit(amount, self.month)
            self.inc_operations()
            return True
        return False

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
