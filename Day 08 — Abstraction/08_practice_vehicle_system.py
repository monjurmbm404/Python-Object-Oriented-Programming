"""
========================================
08_practice_vehicle_system.py
========================================
Practice: Vehicle System
"""

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car is starting with key")

class Bike(Vehicle):
    def start(self):
        print("Bike is starting with kick")

vehicles = [Car(), Bike()]

for v in vehicles:
    v.start()