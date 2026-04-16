"""
========================================
08_practice_vehicle.py
========================================
Practice: Vehicle Example
"""

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(self.brand, "is starting")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)

c = Car("Toyota", "Corolla")

c.start()
c.display()