"""
========================================
08_best_practices.py
========================================
BEST PRACTICES:

✔ Meaningful names
✔ Small functions
✔ No duplicate code
✔ Encapsulation
✔ Separation of concerns
"""

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self, percent):
        return self.price - (self.price * percent / 100)