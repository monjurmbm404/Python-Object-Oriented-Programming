"""
========================================
06_method_overriding.py
========================================
Method Overriding:

✔ Child class modifies parent method
✔ Same method name, different behavior
"""

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Cat(Animal):
    def sound(self):
        print("Cat meows")  # Overriding

a = Animal()
c = Cat()

a.sound()
c.sound()