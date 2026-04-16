"""
========================================
07_practice_animal.py
========================================
Practice: Animal Polymorphism
"""

class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        print("Dog: Bark Bark")

class Cat(Animal):
    def sound(self):
        print("Cat: Meow Meow")

class Cow(Animal):
    def sound(self):
        print("Cow: Moo Moo")

animals = [Dog(), Cat(), Cow(), Animal()]

for animal in animals:
    animal.sound()