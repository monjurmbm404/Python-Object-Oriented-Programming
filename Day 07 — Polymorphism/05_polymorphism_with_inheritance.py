"""
========================================
05_polymorphism_with_inheritance.py
========================================
Polymorphism + Inheritance:

✔ Child modifies parent behavior
"""

class Payment:
    def pay(self):
        print("Processing payment")

class CreditCard(Payment):
    def pay(self):
        print("Paying via Credit Card")

class PayPal(Payment):
    def pay(self):
        print("Paying via PayPal")

methods = [CreditCard(), PayPal(), Payment()]

for method in methods:
    method.pay()