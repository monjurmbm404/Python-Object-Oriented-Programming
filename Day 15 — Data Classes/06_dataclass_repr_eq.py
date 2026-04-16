"""
========================================
06_dataclass_repr_eq.py
========================================
Auto-generated Methods:

✔ __repr__
✔ __eq__
"""

from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    salary: int

e1 = Employee("A", 50000)
e2 = Employee("A", 50000)

print(e1)       # __repr__
print(e1 == e2) # __eq__