"""
========================================
01_exceptions_inside_class.py
========================================
Exceptions inside classes:

✔ Handle errors inside methods
✔ Prevent program crash
"""

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        try:
            if amount > self.balance:
                raise ValueError("Insufficient balance")
            self.balance -= amount
            print("Withdrawal successful:", amount)
        except ValueError as e:
            print("Error:", e)

acc = BankAccount(1000)

acc.withdraw(500)
acc.withdraw(2000)  # triggers exception