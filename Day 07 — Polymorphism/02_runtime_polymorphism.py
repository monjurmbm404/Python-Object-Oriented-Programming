"""
========================================
02_runtime_polymorphism.py
========================================
Runtime Polymorphism:

✔ Method is decided at runtime
✔ Same interface, different behavior
"""

class Shape:
    def area(self):
        print("Calculating area")

class Circle(Shape):
    def area(self):
        print("Area of Circle: πr²")

class Rectangle(Shape):
    def area(self):
        print("Area of Rectangle: l × b")

# Runtime decision
shapes = [Circle(), Rectangle(), Shape()]

for shape in shapes:
    shape.area()