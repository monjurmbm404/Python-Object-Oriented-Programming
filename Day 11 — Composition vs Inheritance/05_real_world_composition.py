"""
========================================
05_real_world_composition.py
========================================
Real-world Composition:

✔ Car HAS Engine, Battery, Wheels
"""

class Engine:
    def start(self):
        print("Engine started")

class Battery:
    def power(self):
        print("Battery supplying power")

class Car:
    def __init__(self):
        self.engine = Engine()
        self.battery = Battery()

    def start_car(self):
        self.battery.power()
        self.engine.start()
        print("Car started successfully")

car = Car()
car.start_car()