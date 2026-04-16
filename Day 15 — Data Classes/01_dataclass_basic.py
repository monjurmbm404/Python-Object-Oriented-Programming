"""
========================================
01_dataclass_basic.py
========================================
@dataclass:

✔ Automatically generates boilerplate code
✔ Like __init__, __repr__, __eq__
✔ Cleaner than normal class
"""

from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
    marks: int

# Object creation (no need to write __init__)
s1 = Student("Monjur", 22, 90)

print(s1)  # auto __repr__