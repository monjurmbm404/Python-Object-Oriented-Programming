"""
========================================
02_product_model.py
========================================
Product Model:

✔ Base product entity
"""

class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

    def __str__(self):
        return f"{self.name} - {self.price}"