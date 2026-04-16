"""
========================================
01_without_slots.py
========================================
Default Python Classes (No __slots__):

✔ Python stores attributes in a dictionary (__dict__)
✔ Flexible but uses more memory
"""

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s = Student("Monjur", 22)

# Normal object stores attributes in __dict__
print(s.__dict__)