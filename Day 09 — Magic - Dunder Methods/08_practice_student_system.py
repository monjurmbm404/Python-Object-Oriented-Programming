"""
========================================
08_practice_student_system.py
========================================
Practice: Student System
"""

class Student:
    def __init__(self, marks):
        self.marks = marks

    def __add__(self, other):
        return Student(self.marks + other.marks)

    def __str__(self):
        return f"Total Marks: {self.marks}"

s1 = Student(80)
s2 = Student(90)

s3 = s1 + s2

print(s3)