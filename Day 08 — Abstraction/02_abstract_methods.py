"""
========================================
02_abstract_methods.py
========================================
Abstract Methods:

✔ Declared but not implemented in parent class
✔ Must be implemented in child class
"""

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass  # No implementation here

# Child class MUST implement abstract method
class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

d = Dog()
c = Cat()

d.sound()
c.sound()