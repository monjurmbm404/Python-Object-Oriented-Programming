"""
========================================
05_multiple_operator_real_world.py
========================================
Multiple Operators Together:

✔ Combine multiple operator overloads
"""

class Cart:
    def __init__(self, items):
        self.items = items

    def __add__(self, other):
        return Cart(self.items + other.items)

    def __len__(self):
        return len(self.items)

    def __eq__(self, other):
        return self.items == other.items

    def __str__(self):
        return f"Cart: {self.items}"

c1 = Cart(["Book", "Pen"])
c2 = Cart(["Laptop"])

c3 = c1 + c2

print(c1)
print(c2)
print(c3)
print("Size:", len(c3))