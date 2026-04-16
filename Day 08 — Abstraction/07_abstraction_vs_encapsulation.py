"""
========================================
07_abstraction_vs_encapsulation.py
========================================
Abstraction vs Encapsulation:

✔ Abstraction → Hides complexity (what to do)
✔ Encapsulation → Hides data (how to protect)
"""

# Abstraction example: only method is shown
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r

c = Circle(5)
print("Area:", c.area())