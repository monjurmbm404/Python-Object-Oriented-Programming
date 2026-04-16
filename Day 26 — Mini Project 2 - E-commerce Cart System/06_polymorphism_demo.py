"""
========================================
06_polymorphism_demo.py
========================================
Polymorphism:

✔ Same method name, different behavior
"""

from 02_physical_product import PhysicalProduct
from 03_digital_product import DigitalProduct

products = [
    PhysicalProduct("Phone", 20000, 300),
    DigitalProduct("Course", 1000)
]

for p in products:
    print(p.name, "->", p.get_price())