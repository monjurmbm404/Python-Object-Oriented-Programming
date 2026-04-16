"""
========================================
01_instance_vs_class_variables.py
========================================
Instance vs Class Variables:

✔ Class variable → shared by all objects
✔ Instance variable → unique for each object
"""

class Student:
    # Class variable (shared)
    school = "ABC School"

    def __init__(self, name):
        # Instance variable (unique per object)
        self.name = name

# Objects
s1 = Student("Monjur")
s2 = Student("Rahim")

print(s1.name, s1.school)
print(s2.name, s2.school)

# Changing class variable affects all objects
Student.school = "XYZ School"

print("After change:")
print(s1.school)
print(s2.school)