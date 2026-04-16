"""
========================================
01_single_inheritance.py
========================================
Single Inheritance:

✔ One child class inherits from one parent class
✔ Child gets all properties & methods of parent
"""

# Parent class
class Animal:
    def eat(self):
        print("Animal is eating")

# Child class inherits from Animal
class Dog(Animal):
    def bark(self):
        print("Dog is barking")

# Create object of child
d = Dog()

# Access parent method
d.eat()

# Access child method
d.bark()