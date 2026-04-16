"""
========================================
04_property_getter.py
========================================
@property:

✔ Turns method into attribute
✔ Cleaner access (no parentheses)
"""

class Product:
    def __init__(self, price):
        self._price = price  # protected variable

    @property
    def price(self):
        return self._price

p = Product(500)

# Access like attribute
print(p.price)