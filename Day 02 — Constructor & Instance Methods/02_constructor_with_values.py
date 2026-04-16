"""
========================================
02_constructor_with_values.py
========================================
Constructor with parameters:

✔ Pass values during object creation
✔ Initialize instance variables
"""

class Student:
    def __init__(self, name, age):
        self.name = name  # instance variable
        self.age = age

# Creating objects with values
s1 = Student("Monjur", 22)
s2 = Student("Rahim", 20)

print(s1.name, s1.age)
print(s2.name, s2.age)