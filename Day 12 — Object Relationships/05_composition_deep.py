"""
========================================
05_composition_deep.py
========================================
Composition (Deep):

✔ Strong ownership
✔ Child object cannot exist independently
✔ Created inside parent
"""

class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        # Composition: created inside
        self.engine = Engine()

    def start(self):
        self.engine.start()
        print("Car running")

c = Car()
c.start()