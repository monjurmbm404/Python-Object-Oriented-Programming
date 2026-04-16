"""
========================================
04_creating_objects.py
========================================
Creating Objects:

✔ Object = instance of class
✔ Each object can have its own data
"""

class Student:
    name = ""
    age = 0

# Creating objects
s1 = Student()
s2 = Student()

# Assign values
s1.name = "Monjur"
s1.age = 22

s2.name = "Rahim"
s2.age = 20

print(s1.name, s1.age)
print(s2.name, s2.age)