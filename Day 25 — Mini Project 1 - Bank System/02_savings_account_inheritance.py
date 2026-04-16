"""
========================================
02_savings_account_inheritance.py
========================================
Inheritance:

✔ SavingsAccount inherits Account
✔ Adds interest feature
"""

from 01_account_base import Account

class SavingsAccount(Account):
    def __init__(self, name, balance, interest_rate):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.get_balance() * self.interest_rate / 100
        self.deposit(interest)
        return f"Interest added: {interest}"