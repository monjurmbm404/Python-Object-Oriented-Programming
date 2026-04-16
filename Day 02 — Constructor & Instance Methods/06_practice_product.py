"""
========================================
06_practice_product.py
========================================
Practice: Product Class
"""

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show(self):
        print("Product:", self.name)
        print("Price:", self.price)

# Create objects
p1 = Product("Laptop", 50000)
p2 = Product("Phone", 20000)

p1.show()
p2.show()