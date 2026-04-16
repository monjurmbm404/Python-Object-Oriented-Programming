"""
========================================
05_inventory_system.py
========================================
Inventory System:

✔ Manages product stock
"""

class Inventory:
    def __init__(self):
        self.stock = {}

    def add_product(self, product, quantity):
        self.stock[product.product_id] = {
            "product": product,
            "qty": quantity
        }

    def is_available(self, product_id):
        return product_id in self.stock and self.stock[product_id]["qty"] > 0