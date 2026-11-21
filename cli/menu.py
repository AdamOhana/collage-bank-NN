from cli.commands import Command
from banking_data.bank import Bank

EXIT_KEY = "0"

class Menu:
    def __init__(self, bank: Bank, commands: dict[str, Command]) -> None:
        self.bank = bank
        self.commands = commands

    def _print_menu(self) -> None:
        print("========== BANK SYSTEM ==========")
        for key, command in self.commands.items():
            print(f"{key}: {command.label}")
        print(f"{EXIT_KEY}: Exit")
    