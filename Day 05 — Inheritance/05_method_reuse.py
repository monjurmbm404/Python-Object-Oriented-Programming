"""
========================================
05_method_reuse.py
========================================
Method Reuse:

✔ Child class reuses parent methods
✔ Avoids rewriting same code
"""

class Calculator:
    def add(self, a, b):
        return a + b

class AdvancedCalculator(Calculator):
    def square(self, x):
        return x * x

calc = AdvancedCalculator()

# Reusing parent method
print("Addition:", calc.add(10, 5))

# Child method
print("Square:", calc.square(4))