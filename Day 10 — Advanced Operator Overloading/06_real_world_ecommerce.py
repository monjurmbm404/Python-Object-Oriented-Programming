"""
========================================
06_real_world_ecommerce.py
========================================
E-commerce Example:

✔ Compare products
✔ Add cart items
"""

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __gt__(self, other):
        return self.price > other.price

    def __add__(self, other):
        return Product("Bundle", self.price + other.price)

    def __str__(self):
        return f"{self.name} - {self.price}"

p1 = Product("Laptop", 50000)
p2 = Product("Mouse", 1000)

print("Expensive:", p1 > p2)

bundle = p1 + p2
print("Bundle:", bundle)