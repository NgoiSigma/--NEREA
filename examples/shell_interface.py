# Σ-NEREA / examples/shell_interface.py

from core.interface_shell import InterfaceShell
from core import fdl_core

if __name__ == "__main__":
    agent = fdl_core.AvatarusSigma()
    shell = InterfaceShell(agent)

    print(shell.welcome())

    while True:
        try:
            query = input("Σ > ")
            result = shell.handle_input(query)
            print(f"⮕ Синтез: {result}")
        except KeyboardInterrupt:
            print("\n[ Завершение сеанса ]")
            break
