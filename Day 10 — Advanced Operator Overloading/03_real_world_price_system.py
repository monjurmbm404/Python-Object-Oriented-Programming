"""
========================================
03_real_world_price_system.py
========================================
Real-world Example:

✔ Compare and calculate product prices
"""

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # Compare prices
    def __gt__(self, other):
        return self.price > other.price

    def __add__(self, other):
        return Item("Combo", self.price + other.price)

    def __str__(self):
        return f"{self.name} - {self.price}"

item1 = Item("Shoes", 3000)
item2 = Item("Bag", 2000)

print(item1 > item2)

combo = item1 + item2
print(combo)