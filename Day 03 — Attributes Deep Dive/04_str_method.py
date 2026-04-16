"""
========================================
04_str_method.py
========================================
__str__():

✔ Used for user-friendly string representation
✔ Called by print()
"""

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Student: {self.name}, Marks: {self.marks}"

s1 = Student("Monjur", 90)

print(s1)  # automatically calls __str__()