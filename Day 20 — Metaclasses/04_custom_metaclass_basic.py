"""
========================================
04_custom_metaclass_basic.py
========================================
Custom Metaclass:

✔ Controls class creation
✔ Can modify class behavior
"""

class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class: {name}")
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=MyMeta):
    def hello(self):
        return "Hello World"

obj = MyClass()
print(obj.hello())