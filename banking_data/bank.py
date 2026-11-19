from account import Account


class Bank:
    account_list: list[Account]

    def __init__(self, account_list: list[Account]):
        self.accounts = account_list

    def show_accounts(self):
        for i in range(len(self.account_list)):
            print(f"index: {i}\n", self.account_list[i].to_dict(), sep="")

    def delete_account(self, index: int):
        if 0 < index < len(self.account_list):
            self.account_list.pop(index)
        else:
            print("Index out of bounds: no such account exists")