"""
========================================
01_product_base.py
========================================
Base Product Class:

✔ Common structure for all products
"""

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

    def display(self):
        return f"{self.name} - {self.price}"