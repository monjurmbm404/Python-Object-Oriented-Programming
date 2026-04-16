"""
========================================
07_testable_class_design.py
========================================
Testable Class Design:

✔ No print inside logic
✔ Return values instead
"""

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

def test_bank():
    acc = BankAccount(1000)
    assert acc.deposit(500) == 1500

test_bank()
print("Bank test passed")