"""
========================================
05_property_setter.py
========================================
@setter:

✔ Controls how value is set
✔ Allows validation
"""

class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            print("Invalid price")
        else:
            self._price = value

p = Product(500)

p.price = 1000
print(p.price)

p.price = -200  # validation