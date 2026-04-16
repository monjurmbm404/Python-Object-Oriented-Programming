"""
========================================
04_slots_attribute_restriction.py
========================================
Restriction of __slots__:

✔ Cannot add new attributes dynamically
"""

class Product:
    __slots__ = ["name", "price"]

    def __init__(self, name, price):
        self.name = name
        self.price = price

p = Product("Laptop", 50000)

print(p.name)

# p.category = "Electronics" ❌ Error (not allowed)