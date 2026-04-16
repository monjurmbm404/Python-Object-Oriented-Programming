"""
========================================
06_str_vs_repr.py
========================================
Difference between __str__ and __repr__:

✔ __str__ → user-friendly output
✔ __repr__ → developer/debug output
"""

class Car:
    def __init__(self, brand):
        self.brand = brand

    def __str__(self):
        return f"Car brand: {self.brand}"

    def __repr__(self):
        return f"Car('{self.brand}')"

c = Car("Tesla")

print(str(c))
print(repr(c))