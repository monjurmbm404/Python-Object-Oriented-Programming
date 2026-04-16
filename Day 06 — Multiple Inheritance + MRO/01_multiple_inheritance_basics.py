"""
========================================
01_multiple_inheritance_basics.py
========================================
Multiple Inheritance:

✔ A class can inherit from multiple parent classes
✔ Child gets features from all parents
"""

class Father:
    def skills(self):
        print("Father: Gardening, Driving")

class Mother:
    def skills(self):
        print("Mother: Cooking, Painting")

# Child inherits from both Father and Mother
class Child(Father, Mother):
    def my_skills(self):
        print("Child: Sports, Coding")

c = Child()

c.my_skills()

# Both parent methods are available
c.skills()  # Which one will run? (important for MRO)