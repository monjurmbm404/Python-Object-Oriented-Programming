"""
========================================
06_liskov_substitution.py
========================================
Liskov Substitution Principle:

✔ Child class should behave like parent
✔ No unexpected behavior
"""

class Bird:
    def fly(self):
        print("Flying")

class Sparrow(Bird):
    pass

# ❌ Problem: Not all birds fly (bad design)
# Penguin should not inherit fly()

class Penguin:
    def swim(self):
        print("Swimming")

# ✔ Better design → separate behavior