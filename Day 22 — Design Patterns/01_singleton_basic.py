"""
========================================
01_singleton_basic.py
========================================
Singleton Pattern:

✔ Only ONE instance of a class exists
✔ Useful for:
    - Database connection
    - Config manager
"""

class Singleton:
    _instance = None  # class variable

    def __new__(cls):
        # __new__ controls object creation
        if cls._instance is None:
            print("Creating new instance")
            cls._instance = super().__new__(cls)
        return cls._instance

# Creating multiple objects
s1 = Singleton()
s2 = Singleton()

print(s1 is s2)  # True → same object