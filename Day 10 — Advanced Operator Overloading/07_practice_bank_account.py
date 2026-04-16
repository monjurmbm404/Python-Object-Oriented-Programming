"""
========================================
07_practice_bank_account.py
========================================
Practice: Bank Account System
"""

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def __add__(self, other):
        return BankAccount(self.balance + other.balance)

    def __sub__(self, other):
        return BankAccount(self.balance - other.balance)

    def __gt__(self, other):
        return self.balance > other.balance

    def __str__(self):
        return f"Balance: {self.balance}"

a1 = BankAccount(1000)
a2 = BankAccount(500)

print(a1 + a2)
print(a1 - a2)
print(a1 > a2)