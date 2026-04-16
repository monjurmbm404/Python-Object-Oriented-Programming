"""
========================================
05_testing_class_methods.py
========================================
Testing Class Methods:
"""

class Calculator:
    def add(self, a, b):
        return a + b

def test_calculator():
    calc = Calculator()
    assert calc.add(2, 3) == 5

test_calculator()
print("Calculator test passed")