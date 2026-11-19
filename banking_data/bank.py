from account import Account

OPERATIONS_PER_MONTH = 10

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

    def delete_account(self, index: int) -> bool:
        if (0 <= index < self.top):
            self.account_list.pop(index)
            self.top -= 1
            return True
        else:
            print("Index out of bounds: no such account exists")
            return False

    def add_money(self, index: int, amount: float) -> bool:
        if not (0 <= index < self.top):
            return False
        
        acc = self.account_list[index]
        acc.balance += amount
        acc.history.append({"type": "deposit", "amount": amount, "month": self.month})
        return True

    def remove_money(self, index: int, amount: float) -> bool:
        if not (0 <= index < self.top):
            return False
        
        acc = self.account_list[index]
        acc.balance -= amount
        acc.history.append({"type": "withdrawal", "amount": amount, "month": self.month})
        return True

    def transfer_to_savings(self, index: int, amount: float) -> bool:
        if not (0 <= index < self.top):
            return False
        
        acc = self.account_list[index]
        acc.savings += amount
        acc.balance -= amount
        acc.history.append({"type": "saving", "amount": amount, "month": self.month})
        return True

    def send_money(self, from_index: int, to_index: int, amount: float) -> bool:
        if not (0 <= from_index < self.top):
            return False
        if not (0 <= to_index < self.top):
            return False
        
        acc1 = self.account_list[from_index]
        acc2 = self.account_list[to_index]
        acc1.balance -= amount
        acc2.balance += amount
        acc1.history.append({"type": "deposit-transfer", "amount": amount, "month": self.month})
        acc2.history.append({"type": "withdrawal-transfer", "amount": amount, "month": self.month})
        return True

    def inc_operations(self) -> None:
        self.operations += 1
        if self.operations % OPERATIONS_PER_MONTH == 0:
            self.month += 1
            self.trigger_savings()
            self.trigger_interest()

    def trigger_savings(self):
        pass

    def trigger_interest(self):
        pass
