"""
========================================
06_practice_bank_account.py
========================================
Practice: BankAccount (Encapsulation)
"""

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # private variable

    # Deposit method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited")
        else:
            print("Invalid amount")

    # Withdraw method
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print(f"{amount} withdrawn")

    # Getter
    def get_balance(self):
        return self.__balance

# Create account
acc = BankAccount("Monjur", 1000)

acc.deposit(500)
acc.withdraw(300)

print("Balance:", acc.get_balance())