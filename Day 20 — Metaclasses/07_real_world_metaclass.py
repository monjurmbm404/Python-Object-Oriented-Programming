"""
========================================
07_real_world_metaclass.py
========================================
Real-world usage:

✔ Frameworks (Django, ORM systems)
✔ Automatic registration
"""

class RegistryMeta(type):
    registry = {}

    def __new__(cls, name, bases, dct):
        new_class = super().__new__(cls, name, bases, dct)
        cls.registry[name] = new_class
        return new_class

class A(metaclass=RegistryMeta):
    pass

class B(metaclass=RegistryMeta):
    pass

print(RegistryMeta.registry)