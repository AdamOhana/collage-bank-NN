"""
This script will be used for manual simulation of the bank.
testing purposes only
"""
from banking_data.bank import Bank
from banking_data.account import Account
from cli.menu import Menu
from cli import commands as cmd

# The following are the default bank and menu fields
bank = Bank([
    Account("Dan", 120),
    Account("Maya", 45, 10),
    Account("Yoshi", 500, 200),
    Account("Noa", 56),
    Account("Avi", 20, 5),
])

commands = {
    "1": cmd.CreateAccount(),
    "2": cmd.ShowAccountsNormal(),
    "3": cmd.DeleteAccount(),
    "4": cmd.DepositMoney(),
    "5": cmd.WithdrawMoney(),
    "6": cmd.TransferToSavings(),
    "7": cmd.SendMoney(),
    "8": cmd.ShowAccountsDict(),
    "9": cmd.ShowAccountsNormal()
}

menu = Menu(bank, commands)

# Begin simulation
if __name__ == "__main__":
    menu.run()
