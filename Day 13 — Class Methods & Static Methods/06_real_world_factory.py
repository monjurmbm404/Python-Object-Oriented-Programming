"""
========================================
06_real_world_factory.py
========================================
Real-world Factory Example:

✔ Create objects from structured data
"""

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = int(price)

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["price"])

data = {"name": "Laptop", "price": "50000"}

p = Product.from_dict(data)

print(p.name, p.price)