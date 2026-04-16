"""
========================================
03_composition_vs_inheritance.py
========================================
Composition vs Inheritance:

✔ Inheritance → tight coupling
✔ Composition → loose coupling (better)
"""

# Inheritance approach
class Bird:
    def fly(self):
        print("Flying")

class Sparrow(Bird):
    pass

# Problem: not all birds fly (bad design)

# Composition approach
class FlyAbility:
    def fly(self):
        print("Flying")

class Bird2:
    def __init__(self, fly_ability=None):
        self.fly_ability = fly_ability

    def perform_fly(self):
        if self.fly_ability:
            self.fly_ability.fly()
        else:
            print("Cannot fly")

b1 = Bird2(FlyAbility())
b2 = Bird2()

b1.perform_fly()
b2.perform_fly()