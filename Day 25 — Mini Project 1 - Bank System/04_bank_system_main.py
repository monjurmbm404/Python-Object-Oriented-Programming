"""
========================================
04_bank_system_main.py
========================================
Main System:

✔ Combine everything
"""

from 01_account_base import Account
from 02_savings_account_inheritance import SavingsAccount
from 03_current_account_inheritance import CurrentAccount

# Basic Account
acc1 = Account("Monjur", 1000)
print(acc1.deposit(500))
print(acc1.withdraw(300))
print("Balance:", acc1.get_balance())

print("\n-------------------\n")

# Savings Account
savings = SavingsAccount("Rahim", 2000, 5)
print(savings.add_interest())
print("Balance:", savings.get_balance())

print("\n-------------------\n")

# Current Account
current = CurrentAccount("Karim", 1000, 500)
print(current.withdraw(1300))  # uses overdraft
print("Balance:", current.get_balance())