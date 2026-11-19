from account import Account


class Bank:
    def __init__(self, account_list: list[Account]):
        self.accounts = account_list
