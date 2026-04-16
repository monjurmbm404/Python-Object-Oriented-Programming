"""
========================================
05_encapsulation_demo.py
========================================
Encapsulation Demo:

✔ Protect internal data
"""

class SecureAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def update_balance(self, amount):
        if amount < 0:
            return "Invalid amount"
        self.__balance += amount

acc = SecureAccount(1000)

print(acc.get_balance())
acc.update_balance(500)
print(acc.get_balance())