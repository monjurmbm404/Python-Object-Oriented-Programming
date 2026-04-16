"""
========================================
01_account_base.py
========================================
Base Class: Account

✔ Encapsulation (private balance)
✔ Common behavior for all accounts
"""

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance  # private variable (encapsulation)

    # Getter
    def get_balance(self):
        return self.__balance

    # Deposit method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited {amount}"
        return "Invalid deposit amount"

    # Withdraw method
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrawn {amount}"
        return "Insufficient balance"