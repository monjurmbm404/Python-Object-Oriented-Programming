"""
========================================
07_combined_property.py
========================================
Combined Property:

✔ Getter + Setter + Deleter together
"""

class Account:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            print("Invalid balance")
        else:
            self._balance = value

    @balance.deleter
    def balance(self):
        print("Balance deleted")
        del self._balance

acc = Account(1000)

print(acc.balance)

acc.balance = 1500
print(acc.balance)

del acc.balance