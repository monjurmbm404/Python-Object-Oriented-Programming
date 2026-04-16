"""
========================================
07_slots_vs_normal.py
========================================
Comparison Summary:

✔ Normal class → flexible, slower, more memory
✔ __slots__ → restricted, faster, memory efficient
"""

class Normal:
    def __init__(self):
        self.a = 10
        self.b = 20

class Slotted:
    __slots__ = ["a", "b"]

    def __init__(self):
        self.a = 10
        self.b = 20

n = Normal()
s = Slotted()

print(n.__dict__)
# print(s.__dict__) ❌ not available