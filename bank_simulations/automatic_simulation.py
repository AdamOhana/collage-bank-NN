"""Automatic simulation: runs random bank operations for N months."""
import random

from banking_data.bank import Bank
from banking_data.account import Account

def _random_amount() -> float:
    return round(random.uniform(1, 200), 2)

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
    _deposit,
    _withdraw,
    _save,
    _send
]

