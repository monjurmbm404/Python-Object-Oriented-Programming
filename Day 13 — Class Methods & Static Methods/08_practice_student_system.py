"""
========================================
08_practice_student_system.py
========================================
Practice: Student System
"""

class Student:
    school = "Default School"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @classmethod
    def change_school(cls, name):
        cls.school = name

    @staticmethod
    def is_pass(marks):
        return marks >= 40

s1 = Student("Monjur", 80)

print(Student.is_pass(s1.marks))

Student.change_school("New School")
print(Student.school)