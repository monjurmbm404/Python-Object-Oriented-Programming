"""
========================================
05_property_basics.py
========================================
Property Decorator:

✔ Cleaner way to use getter/setter
✔ No need to call methods explicitly
"""

class Product:
    def __init__(self):
        self.__price = 0

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            print("Invalid price")
        else:
            self.__price = value

p = Product()

p.price = 500  # setter
print("Price:", p.price)  # getter