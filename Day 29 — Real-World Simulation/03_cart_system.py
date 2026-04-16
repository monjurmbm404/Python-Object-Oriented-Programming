"""
========================================
03_cart_system.py
========================================
Cart System:

✔ Composition (Cart HAS products)
✔ Business logic
"""

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)

    def remove_item(self, product):
        self.items.remove(product)

    def total_price(self):
        return sum(item.get_price() for item in self.items)

    def show_cart(self):
        for item in self.items:
            print(item)