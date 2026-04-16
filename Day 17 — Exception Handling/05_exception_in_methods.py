"""
========================================
05_exception_in_methods.py
========================================
Method-level exception handling:

✔ Each method handles its own errors
"""

class Calculator:
    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            print("Cannot divide by zero")
            return None

calc = Calculator()

print(calc.divide(10, 2))
print(calc.divide(10, 0))