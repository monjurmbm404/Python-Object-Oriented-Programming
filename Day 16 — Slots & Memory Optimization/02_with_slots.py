"""
========================================
02_with_slots.py
========================================
__slots__:

✔ Removes __dict__
✔ Saves memory
✔ Faster attribute access
"""

class Student:
    __slots__ = ["name", "age"]  # fixed attributes only

    def __init__(self, name, age):
        self.name = name
        self.age = age

s = Student("Monjur", 22)

print(s.name)
print(s.age)

# print(s.__dict__) ❌ will not exist