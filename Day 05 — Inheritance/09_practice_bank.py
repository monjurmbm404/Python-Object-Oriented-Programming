"""
========================================
09_practice_bank.py
========================================
Practice: Bank Account with Inheritance
"""

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

class SavingsAccount(Account):
    def add_interest(self, rate):
        interest = self.balance * rate / 100
        self.balance += interest

acc = SavingsAccount("Monjur", 1000)

acc.deposit(500)
acc.add_interest(10)

print("Owner:", acc.owner)
print("Balance:", acc.balance)