"""
========================================
04_super_keyword.py
========================================
super() Keyword:

✔ Used to call parent class methods
✔ Avoids direct class name usage
✔ Useful in inheritance hierarchy
"""

class Animal:
    def __init__(self):
        print("Animal constructor")

    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def __init__(self):
        # Call parent constructor
        super().__init__()
        print("Dog constructor")

    def sound(self):
        # Call parent method
        super().sound()
        print("Dog barks")

d = Dog()
d.sound()