"""
========================================
02_refactored_user_class.py
========================================
✔ Improved Version:

Fixes:
- Clear naming
- Encapsulation
- Separation of logic
"""

class User:
    def __init__(self, name, email, balance=0):
        self.name = name
        self.email = email
        self.balance = balance

    def display(self):
        return f"{self.name} | {self.email} | {self.balance}"

    def add_balance(self, amount):
        if amount > 0:
            self.balance += amount