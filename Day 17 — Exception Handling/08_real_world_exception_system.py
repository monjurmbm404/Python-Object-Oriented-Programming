"""
========================================
08_real_world_exception_system.py
========================================
Real-world system:

✔ Banking + validation + exceptions
"""

class TransactionError(Exception):
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise TransactionError("Deposit must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise TransactionError("Insufficient balance")
        self.balance -= amount

acc = BankAccount(1000)

try:
    acc.deposit(500)
    acc.withdraw(2000)
except TransactionError as e:
    print("Bank Error:", e)