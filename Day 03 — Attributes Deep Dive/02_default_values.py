"""
========================================
02_default_values.py
========================================
Default Values:

✔ Used when no value is provided
✔ Defined in constructor
"""

class Product:
    def __init__(self, name="Unknown", price=0):
        self.name = name
        self.price = price

# Object with values
p1 = Product("Laptop", 50000)

# Object with default values
p2 = Product()

print(p1.name, p1.price)
print(p2.name, p2.price)