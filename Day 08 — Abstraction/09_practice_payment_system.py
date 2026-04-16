"""
========================================
09_practice_payment_system.py
========================================
Practice: Payment System
"""

from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

class Bank(Payment):
    def pay(self, amount):
        print(f"Paid {amount} via Bank Transfer")

class Card(Payment):
    def pay(self, amount):
        print(f"Paid {amount} via Card")

methods = [Bank(), Card()]

for m in methods:
    m.pay(2000)