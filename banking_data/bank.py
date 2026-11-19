from account import Account


class Bank:
    account_list: list[Account]
    top: int
    month: int

    def __init__(self, account_list: list[Account]):
        self.account_list = account_list
        self.top = len(account_list)

    def show_accounts(self) -> None:
        for i in range(self.top):
            print(f"index: {i}\n", self.account_list[i].to_dict(), sep="")

    def delete_account(self, index: int) -> bool:
        if 0 < index < self.top:
            self.account_list.pop(index)
            self.top -= 1
            return True
        else:
            print("Index out of bounds: no such account exists")
            return False

    def add_money(self, index: int, amount: float) -> bool:
        if not (0 < index < self.top):
            return False
        acc = self.account_list[index]
        acc._balance += amount
        acc._history += {"type": "deposit", "amount": amount, "month": self.month}
        return True

    def remove_money(self, index: int, amount: float) -> bool:
        if not (0 < index < self.top):
            return False
        acc = self.account_list[index]
        acc._balance += amount
        acc._history += {"type": "withdrawal", "amount": amount, "month": self.month}
        return True
