"""
========================================
06_practice_shape.py
========================================
Practice: Shape System
"""

class Shape:
    def area(self):
        print("Calculating area")

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        print("Circle Area:", 3.14 * self.r * self.r)

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        print("Square Area:", self.side * self.side)

shapes = [Circle(5), Square(4)]

for shape in shapes:
    shape.area()