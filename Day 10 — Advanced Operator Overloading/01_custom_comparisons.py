"""
========================================
01_custom_comparisons.py
========================================
Custom Comparisons:

✔ Override comparison operators
✔ Control how objects are compared
"""

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # Greater than >
    def __gt__(self, other):
        return self.price > other.price

    # Less than <
    def __lt__(self, other):
        return self.price < other.price

    # Equal ==
    def __eq__(self, other):
        return self.price == other.price

p1 = Product("Laptop", 50000)
p2 = Product("Phone", 20000)

print(p1 > p2)   # True
print(p1 < p2)   # False
print(p1 == p2)  # False