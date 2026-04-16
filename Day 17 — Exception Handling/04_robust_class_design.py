"""
========================================
04_robust_class_design.py
========================================
Robust Class Design:

✔ Proper validation
✔ Safe error handling
"""

class Product:
    def __init__(self, name, price):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.name = name
        self.price = price

    def apply_discount(self, percent):
        if percent < 0 or percent > 100:
            raise ValueError("Invalid discount percentage")

        discount = (self.price * percent) / 100
        self.price -= discount

p = Product("Laptop", 50000)

try:
    p.apply_discount(10)
    print("New Price:", p.price)

    p.apply_discount(200)  # invalid
except ValueError as e:
    print("Error:", e)