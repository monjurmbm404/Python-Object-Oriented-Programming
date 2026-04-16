"""
========================================
03_before_refactor_bank.py
========================================
❌ BAD DESIGN:

- Mixed logic
- No validation
"""

class Bank:
    def __init__(self):
        self.users = []

    def add(self, name, balance):
        self.users.append([name, balance])

    def show(self):
        for u in self.users:
            print(u[0], u[1])