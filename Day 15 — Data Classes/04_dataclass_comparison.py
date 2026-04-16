"""
========================================
04_dataclass_comparison.py
========================================
Comparison Feature:

✔ Automatically generates __eq__
✔ Objects can be compared easily
"""

from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(2, 3)

print(p1 == p2)  # True
print(p1 == p3)  # False