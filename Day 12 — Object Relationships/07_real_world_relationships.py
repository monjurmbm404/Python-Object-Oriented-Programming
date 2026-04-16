"""
========================================
07_real_world_relationships.py
========================================
Real-world Relationships:

✔ School system example
"""

class Student:
    def __init__(self, name):
        self.name = name

class Classroom:
    def __init__(self):
        self.students = []  # aggregation

    def add_student(self, student):
        self.students.append(student)

    def show(self):
        for s in self.students:
            print(s.name)

class School:
    def __init__(self):
        self.classroom = Classroom()  # composition

school = School()

# Students exist independently → aggregation
s1 = Student("Monjur")
s2 = Student("Rahim")

school.classroom.add_student(s1)
school.classroom.add_student(s2)

school.classroom.show()