"""
========================================
09_practice_large_system.py
========================================
Practice: Large-scale system idea

✔ Optimized object creation using __slots__
"""

class Product:
    __slots__ = ["name", "price"]

    def __init__(self, name, price):
        self.name = name
        self.price = price

products = [Product("Laptop", 50000), Product("Phone", 20000)]

for p in products:
    print(p.name, p.price)