"""
========================================
02_diamond_problem.py
========================================
Diamond Problem:

✔ Happens in multiple inheritance
✔ Same method exists in multiple parent classes
✔ Python resolves using MRO
"""

class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(A):
    def show(self):
        print("Class C")

# D inherits from both B and C (diamond shape)
class D(B, C):
    pass

d = D()

# Which show() will run? → MRO decides
d.show()