"""
========================================
09_practice_bank_property.py
========================================
Practice: Bank Property System
"""

class Bank:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            print("Invalid transaction")
        else:
            self._balance = amount

bank = Bank(2000)

print(bank.balance)

bank.balance = 3000
print(bank.balance)

bank.balance = -100