"""
========================================
05_repr_method.py
========================================
__repr__():

✔ Used for debugging
✔ More technical representation
"""

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product(name='{self.name}', price={self.price})"

p1 = Product("Laptop", 50000)

print(repr(p1))
print(p1)