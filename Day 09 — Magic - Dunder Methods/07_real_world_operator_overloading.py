"""
========================================
07_real_world_operator_overloading.py
========================================
Real-world Example:

✔ Money system using operator overloading
"""

class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Money(self.amount + other.amount)

    def __str__(self):
        return f"Total Money: {self.amount}"

m1 = Money(500)
m2 = Money(300)

m3 = m1 + m2

print(m3)