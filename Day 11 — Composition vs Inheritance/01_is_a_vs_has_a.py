"""
========================================
01_is_a_vs_has_a.py
========================================
"is-a" vs "has-a":

✔ is-a → Inheritance (Child IS A Parent)
✔ has-a → Composition (Class HAS another class)
"""

# Inheritance (is-a relationship)
class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):  # Dog IS-A Animal
    def bark(self):
        print("Barking")

d = Dog()
d.eat()
d.bark()

# Composition (has-a relationship)
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()  # Car HAS-A Engine

    def drive(self):
        self.engine.start()
        print("Car is driving")

c = Car()
c.drive()