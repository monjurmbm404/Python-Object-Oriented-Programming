"""
========================================
02_association_multiple_objects.py
========================================
Association with multiple objects:

✔ One object interacts with many others
✔ No ownership relationship
"""

class Driver:
    def drive(self):
        print("Driving vehicle")

class Car:
    def start(self):
        print("Car started")

class Person:
    def use(self, driver, car):
        # Person associates with Driver & Car
        driver.drive()
        car.start()
        print("Person is traveling")

d = Driver()
c = Car()
p = Person()

p.use(d, c)