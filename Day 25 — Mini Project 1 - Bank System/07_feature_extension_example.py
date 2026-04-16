"""
========================================
07_feature_extension_example.py
========================================
OOP Power:

✔ Easy to extend system
"""

from 01_account_base import Account

class PremiumAccount(Account):
    def bonus(self):
        return "Premium bonus applied!"

acc = PremiumAccount("User", 5000)

print(acc.deposit(1000))
print(acc.bonus())