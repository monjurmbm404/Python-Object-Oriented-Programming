"""
========================================
09_real_world_clean_design.py
========================================
Clean Design Example:

✔ DRY + KISS + SOLID combined
"""

class Payment:
    def pay(self, amount):
        pass

class CardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} via Card")

class CashPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} via Cash")

def process_payment(method, amount):
    method.pay(amount)

process_payment(CardPayment(), 1000)
process_payment(CashPayment(), 500)