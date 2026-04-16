"""
========================================
08_practice_payment_system.py
========================================
Practice: Payment System
"""

class Payment:
    def pay(self):
        print("Generic payment")

class Card(Payment):
    def pay(self):
        print("Paid using Card")

class UPI(Payment):
    def pay(self):
        print("Paid using UPI")

class Cash(Payment):
    def pay(self):
        print("Paid using Cash")

methods = [Card(), UPI(), Cash()]

for m in methods:
    m.pay()