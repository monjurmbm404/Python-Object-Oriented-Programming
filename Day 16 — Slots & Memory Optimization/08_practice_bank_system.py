"""
========================================
08_practice_bank_system.py
========================================
Practice: Bank System Optimization
"""

class BankAccount:
    __slots__ = ["owner", "balance"]

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

acc = BankAccount("Monjur", 1000)

acc.deposit(500)

print(acc.owner, acc.balance)