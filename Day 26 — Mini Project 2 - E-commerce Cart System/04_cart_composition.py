"""
========================================
04_cart_composition.py
========================================
Cart System:

✔ Composition → Cart HAS Products
✔ Not inheritance
"""

class Cart:
    def __init__(self):
        self.items = []  # composition (HAS-A relationship)

    def add_product(self, product):
        self.items.append(product)

    def remove_product(self, product):
        self.items.remove(product)

    def total_price(self):
        total = 0
        for item in self.items:
            total += item.get_price()
        return total

    def show_items(self):
        for item in self.items:
            print(item.display())