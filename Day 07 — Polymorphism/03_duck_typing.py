"""
========================================
03_duck_typing.py
========================================
Duck Typing:

✔ "If it behaves like a duck, it's a duck"
✔ No need for strict type checking
"""

class Car:
    def move(self):
        print("Car is moving")

class Plane:
    def move(self):
        print("Plane is flying")

class Person:
    def move(self):
        print("Person is walking")

# Function accepts any object with move()
def start_movement(obj):
    obj.move()

start_movement(Car())
start_movement(Plane())
start_movement(Person())