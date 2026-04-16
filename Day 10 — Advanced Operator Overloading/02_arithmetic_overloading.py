"""
========================================
02_arithmetic_overloading.py
========================================
Arithmetic Operator Overloading:

✔ Customize + - * / behavior
"""

class Money:
    def __init__(self, amount):
        self.amount = amount

    # Addition
    def __add__(self, other):
        return Money(self.amount + other.amount)

    # Subtraction
    def __sub__(self, other):
        return Money(self.amount - other.amount)

    # Multiplication
    def __mul__(self, other):
        return Money(self.amount * other.amount)

    # Division
    def __truediv__(self, other):
        return Money(self.amount / other.amount)

    def __str__(self):
        return f"Money: {self.amount}"

m1 = Money(1000)
m2 = Money(200)

print(m1 + m2)
print(m1 - m2)
print(m1 * m2)
print(m1 / m2)