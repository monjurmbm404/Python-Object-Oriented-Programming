"""
========================================
05_multiple_objects.py
========================================
Multiple Objects:

✔ Each object has its own data
✔ Same class, different values
"""

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(self.name, "scored", self.marks)

# Multiple objects
s1 = Student("Monjur", 90)
s2 = Student("Karim", 85)
s3 = Student("Rahim", 88)

s1.display()
s2.display()
s3.display()