"""
========================================
07_combined_example.py
========================================
Combined Example:

✔ classmethod + staticmethod together
"""

class Account:
    bank_name = "ABC Bank"

    def __init__(self, balance):
        self.balance = balance

    @classmethod
    def change_bank(cls, name):
        cls.bank_name = name

    @staticmethod
    def is_valid_amount(amount):
        return amount > 0

# Use static method
print(Account.is_valid_amount(100))
print(Account.is_valid_amount(-50))

# Use class method
Account.change_bank("XYZ Bank")
print(Account.bank_name)