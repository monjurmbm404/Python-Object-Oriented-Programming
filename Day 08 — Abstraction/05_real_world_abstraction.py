"""
========================================
05_real_world_abstraction.py
========================================
Real-world Abstraction:

✔ User doesn't care how payment works internally
✔ Only cares about pay() function
"""

from abc import ABC, abstractmethod

class BankApp(ABC):

    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def transfer_money(self, amount):
        pass

class MobileBanking(BankApp):

    def login(self):
        print("User logged in via Mobile App")

    def transfer_money(self, amount):
        print(f"Transferred {amount} via Mobile Banking")

app = MobileBanking()

app.login()
app.transfer_money(5000)