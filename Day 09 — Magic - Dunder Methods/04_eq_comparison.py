"""
========================================
04_eq_comparison.py
========================================
__eq__:

✔ Defines == comparison behavior
"""

class Product:
    def __init__(self, price):
        self.price = price

    def __eq__(self, other):
        return self.price == other.price

p1 = Product(100)
p2 = Product(100)
p3 = Product(200)

print(p1 == p2)  # True
print(p1 == p3)  # False