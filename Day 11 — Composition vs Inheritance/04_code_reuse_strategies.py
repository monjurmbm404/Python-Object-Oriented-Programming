"""
========================================
04_code_reuse_strategies.py
========================================
Code Reuse Strategies:

✔ Inheritance → reuse by extending class
✔ Composition → reuse by combining objects
"""

# Inheritance reuse
class Calculator:
    def add(self, a, b):
        return a + b

class AdvancedCalculator(Calculator):
    def square(self, x):
        return x * x

calc = AdvancedCalculator()
print(calc.add(5, 3))
print(calc.square(4))

# Composition reuse
class Adder:
    def add(self, a, b):
        return a + b

class App:
    def __init__(self):
        self.adder = Adder()

    def compute(self):
        return self.adder.add(10, 20)

app = App()
print(app.compute())