"""
========================================
03_slots_memory_comparison.py
========================================
Memory Comparison:

✔ Normal class → uses dictionary per object
✔ __slots__ → fixed memory layout
"""

import sys

class NormalStudent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class SlottedStudent:
    __slots__ = ["name", "age"]

    def __init__(self, name, age):
        self.name = name
        self.age = age

n = NormalStudent("A", 20)
s = SlottedStudent("A", 20)

print("Normal size:", sys.getsizeof(n))
print("Slotted size:", sys.getsizeof(s))