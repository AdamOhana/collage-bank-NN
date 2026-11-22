"""Automatic simulation: runs random bank operations for N months."""
import random

from banking_data.bank import Bank
from banking_data.account import Account
from model.bank_brain import BankModel


def _random_amount() -> float:
    return round(random.uniform(1, 30), 2)

def _deposit(bank: Bank) -> None:
    bank.add_money(random.randint(0, len(bank.account_list)), _random_amount())

def _withdraw(bank: Bank) -> None:
    bank.remove_money(random.randint(0, len(bank.account_list)), _random_amount())

def _save(bank: Bank) -> None:
    bank.transfer_to_savings(random.randint(0, len(bank.account_list)), _random_amount())

def _send(bank: Bank) -> None:
    bank.send_money(random.randint(0, len(bank.account_list)), random.randint(0, len(bank.account_list)), _random_amount())

ACTIONS = [
    _deposit,
    _deposit,
    _withdraw,
    _withdraw,
    _save,
    _send
]

def simulate(bank: Bank, months: int) -> None:
    target_month = bank.month + months
    while bank.month < target_month:
        action = random.choice(ACTIONS)
        try:
            action(bank)
        except (ValueError, IndexError):
            pass

def evaluate(model: BankModel) -> None:
    model.epsilon = 0   # no random exploration, show the network's real choice
    for b in (20, 30, 40, 49, 50, 51, 55, 56, 57, 60, 70, 100, 160, 166, 167, 200, 500):
        print(b, model.pick_action(Account("t", b)))


def main() -> BankModel:
    bank = Bank([
        Account("Dan", 120),
        Account("Maya", 45, 10),
        Account("Yoshi", 500, 200),
        Account("Noa", 56),
        Account("Avi", 20, 5),
    ])
    months = int(input("Months to simulate: "))
    simulate(bank, months)
    bank.show_accounts_normal()
    print(f"Month: {bank.month}, successful operations: {bank.operations}")

    return bank.model

if __name__ == "__main__":
    evaluate(main())