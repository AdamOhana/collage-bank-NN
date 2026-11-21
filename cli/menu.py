from cli.commands import Command
from banking_data.bank import Bank

EXIT_KEY = "0"

class Menu:
    def __init__(self, bank: Bank, commands: dict[str, Command]) -> None:
        self.bank = bank
        self.commands = commands

