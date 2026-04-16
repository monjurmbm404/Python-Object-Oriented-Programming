"""
========================================
07_interface_segregation.py
========================================
Interface Segregation Principle:

✔ Don't force unused methods
"""

# ❌ BAD
class Worker:
    def work(self):
        pass

    def eat(self):
        pass

# ✔ GOOD
class Workable:
    def work(self):
        pass

class Eatable:
    def eat(self):
        pass