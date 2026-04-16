"""
========================================
07_practice_order_system.py
========================================
Practice: Order System
"""

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def total_price(self):
        total = sum(p.price for p in self.products)
        return total

o = Order()

o.add_product(Product("Laptop", 50000))
o.add_product(Product("Mouse", 1000))

print("Total:", o.total_price())