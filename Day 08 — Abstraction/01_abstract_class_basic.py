"""
========================================
01_abstract_class_basic.py
========================================
Abstraction:

✔ Hides implementation details
✔ Shows only essential features
✔ Achieved using abstract classes
"""

from abc import ABC

# Abstract base class (cannot create object directly)
class Vehicle(ABC):
    pass

# This is still incomplete abstraction
v = Vehicle()  # ❌ Not useful, but allowed if no abstract methods
print("Abstract class created (not useful alone)")