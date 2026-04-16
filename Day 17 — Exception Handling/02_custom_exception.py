"""
========================================
02_custom_exception.py
========================================
Custom Exceptions:

✔ Create your own error types
✔ Improve readability & control
"""

class InvalidAgeError(Exception):
    pass

class Person:
    def __init__(self, name, age):
        if age < 0:
            raise InvalidAgeError("Age cannot be negative")
        self.name = name
        self.age = age

try:
    p = Person("Monjur", -5)
except InvalidAgeError as e:
    print("Custom Error:", e)