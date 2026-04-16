"""
========================================
04_instance_methods.py
========================================
Instance Methods:

✔ Methods that work on object data
✔ Must use 'self'
"""

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def multiply(self):
        return self.a * self.b

# Creating object
calc = Calculator(10, 5)

print("Add:", calc.add())
print("Multiply:", calc.multiply())