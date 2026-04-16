"""
========================================
03_custom_exception_with_class_logic.py
========================================
Custom Exception inside class logic:

✔ Better validation design
"""

class InsufficientBalanceError(Exception):
    pass

class Account:
    def __init__(self, balance):
        self.balance = balance

    def transfer(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError("Not enough balance for transfer")
        self.balance -= amount
        print("Transfer successful:", amount)

acc = Account(1000)

try:
    acc.transfer(1500)
except InsufficientBalanceError as e:
    print("Transaction Failed:", e)