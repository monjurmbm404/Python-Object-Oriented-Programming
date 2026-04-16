"""
========================================
07_mro_explanation_flow.py
========================================
MRO Flow Understanding:

✔ Left to right priority
✔ Parent classes checked before grandparent
"""

class A:
    def process(self):
        print("A process")

class B(A):
    def process(self):
        print("B process")

class C(A):
    def process(self):
        print("C process")

class D(B, C):
    pass

d = D()

# Step-by-step resolution
print("MRO Order:", D.mro())

# Executes B first (left priority)
d.process()