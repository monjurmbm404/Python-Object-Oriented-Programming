"""
========================================
07_combined_example.py
========================================
Combined Patterns:

✔ Factory + Strategy together
"""

class Card:
    def pay(self, amount):
        print("Card:", amount)

class Cash:
    def pay(self, amount):
        print("Cash:", amount)

class PaymentFactory:
    @staticmethod
    def get_method(method):
        if method == "card":
            return Card()
        return Cash()

class PaymentProcessor:
    def __init__(self, method):
        self.strategy = PaymentFactory.get_method(method)

    def process(self, amount):
        self.strategy.pay(amount)

p = PaymentProcessor("card")
p.process(1000)