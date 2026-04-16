"""
========================================
03_mro_method.py
========================================
Method Resolution Order (MRO):

✔ Defines order in which classes are searched
✔ Python uses C3 linearization algorithm
"""

class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

d = D()

# Show method resolution order
print(D.mro())

# or alternative
print(D.__mro__)

d.show()