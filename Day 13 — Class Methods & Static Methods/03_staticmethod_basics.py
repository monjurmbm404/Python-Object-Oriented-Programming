"""
========================================
03_staticmethod_basics.py
========================================
@staticmethod:

✔ No access to self or cls
✔ Works like normal function inside class
✔ Used for utility/helper functions
"""

class MathUtils:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def square(x):
        return x * x

print(MathUtils.add(5, 3))
print(MathUtils.square(4))