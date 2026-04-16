"""
========================================
03_self_keyword.py
========================================
self Keyword (IMPORTANT):

✔ Refers to current object
✔ Used to access instance variables & methods
✔ Must be first parameter in instance methods
"""

class Car:
    def __init__(self, brand, speed):
        self.brand = brand   # current object's brand
        self.speed = speed

    def show(self):
        # Accessing object's own data
        print("Brand:", self.brand)
        print("Speed:", self.speed)

# Creating object
c1 = Car("Tesla", 200)

# Calling method
c1.show()