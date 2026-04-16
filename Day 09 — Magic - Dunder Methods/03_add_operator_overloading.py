"""
========================================
03_add_operator_overloading.py
========================================
__add__:

✔ Overloads + operator
✔ Defines custom addition logic
"""

class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

n1 = Number(10)
n2 = Number(20)

result = n1 + n2

print("Result:", result.value)