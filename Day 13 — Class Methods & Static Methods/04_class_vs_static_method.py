"""
========================================
04_class_vs_static_method.py
========================================
Difference:

✔ classmethod → works with class (cls)
✔ staticmethod → no class or object reference
"""

class Demo:
    value = 10

    @classmethod
    def show_class(cls):
        print("Class value:", cls.value)

    @staticmethod
    def show_static():
        print("Static method (no class access)")

Demo.show_class()
Demo.show_static()