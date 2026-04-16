"""
========================================
01_association_basic.py
========================================
Association:

✔ Loose relationship between objects
✔ Objects can exist independently
✔ "uses-a" relationship
"""

class Teacher:
    def __init__(self, name):
        self.name = name

    def teach(self):
        print(self.name, "is teaching")

class Student:
    def __init__(self, name):
        self.name = name

    def learn(self, teacher):
        # Association: Student uses Teacher
        print(self.name, "is learning from", teacher.name)
        teacher.teach()

t = Teacher("Mr. Rahman")
s = Student("Monjur")

s.learn(t)