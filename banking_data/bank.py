from account import Account


class Bank:
    account_list: list[Account]
    top: int
    def __init__(self, account_list: list[Account]):
        self.account_list = account_list
        self.top = len(account_list)

    def show_accounts(self):
        for i in range(self.top):
            print(f"index: {i}\n", self.account_list[i].to_dict(), sep="")

    def delete_account(self, index: int):
        if 0 < index < self.top:
            self.account_list.pop(index)
            self.top -= 1
        else:
            print("Index out of bounds: no such account exists")

