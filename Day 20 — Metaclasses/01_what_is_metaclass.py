"""
========================================
01_what_is_metaclass.py
========================================
What is a Metaclass?

✔ In Python:
    Everything is an object
    Classes are also objects

✔ Metaclass = "Class of a class"
✔ It defines HOW a class is created
"""

# Normal class
class Student:
    pass

# Check type of class
print(type(Student))  # <class 'type'>