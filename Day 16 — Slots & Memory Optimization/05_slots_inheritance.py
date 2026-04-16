"""
========================================
05_slots_inheritance.py
========================================
__slots__ with Inheritance:

✔ Must define slots in parent and child separately
"""

class Animal:
    __slots__ = ["name"]

    def __init__(self, name):
        self.name = name

class Dog(Animal):
    __slots__ = ["breed"]

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

d = Dog("Tommy", "Labrador")

print(d.name)
print(d.breed)