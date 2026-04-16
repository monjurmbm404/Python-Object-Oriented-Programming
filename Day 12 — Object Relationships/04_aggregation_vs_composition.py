"""
========================================
04_aggregation_vs_composition.py
========================================
Aggregation vs Composition:

✔ Aggregation → weak ownership
✔ Composition → strong ownership
"""

# Aggregation example
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self, engine):
        self.engine = engine  # passed from outside (aggregation)

# Engine can exist without Car
engine = Engine()
car = Car(engine)

car.engine.start()