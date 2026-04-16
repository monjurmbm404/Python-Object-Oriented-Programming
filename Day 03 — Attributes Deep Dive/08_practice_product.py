"""
========================================
08_practice_product.py
========================================
Practice: Product Class
"""

class Product:
    category = "General"

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product(name={self.name}, price={self.price}, category={self.category})"

p1 = Product("Phone", 20000)
p2 = Product("Laptop", 50000)

print(p1)
print(p2)