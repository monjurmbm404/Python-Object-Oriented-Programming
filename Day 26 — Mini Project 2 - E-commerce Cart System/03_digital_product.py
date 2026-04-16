"""
========================================
03_digital_product.py
========================================
Digital Product:

✔ No shipping cost
✔ Example: Software, E-book
"""

from 01_product_base import Product

class DigitalProduct(Product):
    def get_price(self):
        # Polymorphism: no extra cost
        return self.price