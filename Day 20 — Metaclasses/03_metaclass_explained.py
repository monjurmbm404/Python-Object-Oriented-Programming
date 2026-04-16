"""
========================================
03_metaclass_explained.py
========================================
Metaclass Concept:

✔ class → creates objects
✔ metaclass → creates classes
✔ default metaclass in Python = type
"""

class MyClass:
    pass

# MyClass is created by metaclass "type"
print(type(MyClass))
print(type(type))  # type is also a metaclass