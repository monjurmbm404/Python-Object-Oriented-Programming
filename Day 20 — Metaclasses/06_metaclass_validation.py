"""
========================================
06_metaclass_validation.py
========================================
Validation using Metaclass:

✔ Enforce rules at class creation
"""

class NoEmptyClassMeta(type):
    def __new__(cls, name, bases, dct):

        if len(dct) == 0:
            raise Exception("Class cannot be empty!")

        return super().__new__(cls, name, bases, dct)

class ValidClass(metaclass=NoEmptyClassMeta):
    x = 10  # must have at least one attribute