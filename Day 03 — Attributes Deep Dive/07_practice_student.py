"""
========================================
07_practice_student.py
========================================
Practice: Student Class
"""

class Student:
    school = "Green Valley School"

    def __init__(self, name, marks=0):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"{self.name} - {self.marks} marks - {self.school}"

# Objects
s1 = Student("Monjur", 95)
s2 = Student("Rahim")

print(s1)
print(s2)