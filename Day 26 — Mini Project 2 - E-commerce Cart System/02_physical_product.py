"""
========================================
02_physical_product.py
========================================
Physical Product:

✔ Example: Laptop, Phone
✔ Adds shipping cost
"""

from 01_product_base import Product

class PhysicalProduct(Product):
    def __init__(self, name, price, shipping_cost):
        super().__init__(name, price)
        self.shipping_cost = shipping_cost

    def get_price(self):
        # Polymorphism: override method
        return self.price + self.shipping_cost