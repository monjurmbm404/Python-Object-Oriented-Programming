"""
========================================
05_metaclass_modifying_class.py
========================================
Metaclass modifying class:

✔ Can inject methods automatically
"""

class AutoAddMethod(type):
    def __new__(cls, name, bases, dct):

        # Inject new method into class
        dct["auto_method"] = lambda self: "Injected Method"

        return super().__new__(cls, name, bases, dct)

class Test(metaclass=AutoAddMethod):
    pass

t = Test()

print(t.auto_method())