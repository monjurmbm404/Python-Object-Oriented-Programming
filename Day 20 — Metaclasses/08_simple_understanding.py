"""
========================================
08_simple_understanding.py
========================================
Simple mental model:

✔ class = blueprint for objects
✔ metaclass = blueprint for classes
"""

class MyMeta(type):
    pass

class MyClass(metaclass=MyMeta):
    pass

print(type(MyClass))   # MyMeta
print(type(MyMeta))    # type