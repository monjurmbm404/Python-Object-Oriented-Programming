"""
========================================
01_constructor_init.py
========================================
__init__ Constructor:

✔ Special method (dunder method)
✔ Automatically called when object is created
✔ Used to initialize object data
"""

class Student:
    def __init__(self):
        print("Constructor called!")

# Creating object → constructor runs automatically
s1 = Student()