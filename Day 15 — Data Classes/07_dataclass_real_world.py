"""
========================================
07_dataclass_real_world.py
========================================
Real-world Example:

✔ Clean model for data handling
"""

from dataclasses import dataclass

@dataclass
class Order:
    item: str
    price: int
    quantity: int = 1

    def total(self):
        return self.price * self.quantity

o = Order("Laptop", 50000, 2)

print(o)
print("Total:", o.total())