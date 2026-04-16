"""
========================================
02_dataclass_init_auto.py
========================================
Auto-generated __init__:

✔ Dataclass automatically creates constructor
"""

from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: int

p = Product("Laptop", 50000)

print(p.name)
print(p.price)