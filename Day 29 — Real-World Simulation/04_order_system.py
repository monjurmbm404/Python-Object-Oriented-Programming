"""
========================================
04_order_system.py
========================================
Order System:

✔ Converts cart → order
"""

class Order:
    def __init__(self, user, cart):
        self.user = user
        self.cart = cart
        self.total = cart.total_price()
        self.status = "PENDING"

    def confirm_order(self):
        self.status = "CONFIRMED"

    def __str__(self):
        return f"Order by {self.user.name} | Total: {self.total} | Status: {self.status}"