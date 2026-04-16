"""
========================================
01_method_overriding.py
========================================
Method Overriding:

✔ Same method name in parent and child class
✔ Child class changes behavior of method
"""

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

# Objects
a = Animal()
d = Dog()
c = Cat()

a.sound()
d.sound()
c.sound()