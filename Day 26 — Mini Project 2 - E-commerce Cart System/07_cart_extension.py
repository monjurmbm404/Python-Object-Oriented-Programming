"""
========================================
07_cart_extension.py
========================================
Extensible Design:

✔ Easy to add new product types
"""

class SubscriptionProduct:
    def __init__(self, name, monthly_fee):
        self.name = name
        self.monthly_fee = monthly_fee

    def get_price(self):
        return self.monthly_fee

    def display(self):
        return f"{self.name} Subscription - {self.monthly_fee}"