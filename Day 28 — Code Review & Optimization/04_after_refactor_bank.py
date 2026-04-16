"""
========================================
04_after_refactor_bank.py
========================================
✔ Improved Design:

Fixes:
- Uses class objects
- Better structure
- Cleaner logic
"""

class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance


class Bank:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def show_users(self):
        for user in self.users:
            print(user.name, user.balance)