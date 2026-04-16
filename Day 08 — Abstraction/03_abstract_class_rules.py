"""
========================================
03_abstract_class_rules.py
========================================
Rules of Abstract Class:

✔ Cannot create object of abstract class
✔ Must implement all abstract methods
"""

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

# ❌ Cannot instantiate abstract class
# s = Shape()

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        print("Circle Area:", 3.14 * self.r * self.r)

c = Circle(5)
c.area()