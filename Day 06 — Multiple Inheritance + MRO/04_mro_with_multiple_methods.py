"""
========================================
04_mro_with_multiple_methods.py
========================================
MRO with multiple methods:

✔ Python searches left to right
✔ First match wins
"""

class A:
    def display(self):
        print("A display")

class B:
    def display(self):
        print("B display")

class C:
    def display(self):
        print("C display")

class D(B, C, A):
    pass

obj = D()

# B will be called first (left to right)
obj.display()

print(D.mro())