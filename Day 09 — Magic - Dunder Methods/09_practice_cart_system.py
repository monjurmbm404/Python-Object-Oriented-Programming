"""
========================================
09_practice_cart_system.py
========================================
Practice: Cart System
"""

class Cart:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __add__(self, other):
        return Cart(self.items + other.items)

    def __str__(self):
        return f"Cart Items: {self.items}"

c1 = Cart(["Book", "Pen"])
c2 = Cart(["Laptop"])

c3 = c1 + c2

print(c1)
print(len(c1))
print(c3)