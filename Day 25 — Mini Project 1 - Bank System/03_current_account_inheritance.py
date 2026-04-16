"""
========================================
03_current_account_inheritance.py
========================================
Another Inheritance Example
"""

from 01_account_base import Account

class CurrentAccount(Account):
    def __init__(self, name, balance, overdraft_limit):
        super().__init__(name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.get_balance() + self.overdraft_limit:
            return super().withdraw(amount)
        return "Overdraft limit exceeded"