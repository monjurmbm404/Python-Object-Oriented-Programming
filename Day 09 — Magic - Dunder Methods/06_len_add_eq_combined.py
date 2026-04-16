"""
========================================
06_len_add_eq_combined.py
========================================
Combined Dunder Methods:

✔ __len__
✔ __add__
✔ __eq__
"""

class Box:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __add__(self, other):
        return Box(self.items + other.items)

    def __eq__(self, other):
        return self.items == other.items

b1 = Box([1, 2, 3])
b2 = Box([4, 5])

b3 = b1 + b2

print("Box size:", len(b1))
print("Merged box:", b3.items)
print("Equal?", b1 == b2)