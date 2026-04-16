"""
========================================
08_real_world_design.py
========================================
Real-world Idea:

✔ Amazon-like cart system
"""

class Cart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def checkout(self):
        return sum(item.get_price() for item in self.items)