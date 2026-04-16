"""
========================================
04_interface_like_design.py
========================================
Interface-like Design:

✔ Python does not have real interfaces
✔ Abstract classes are used as interfaces
"""

from abc import ABC, abstractmethod

class PaymentGateway(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(PaymentGateway):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")

class PayPal(PaymentGateway):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal")

# Polymorphism + abstraction
payments = [CreditCard(), PayPal()]

for p in payments:
    p.pay(1000)