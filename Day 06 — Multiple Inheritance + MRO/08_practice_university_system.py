"""
========================================
08_practice_university_system.py
========================================
Practice: University System
"""

class Person:
    def info(self):
        print("Person info")

class Teacher:
    def teach(self):
        print("Teaching students")

class Researcher:
    def research(self):
        print("Doing research")

class Professor(Teacher, Researcher, Person):
    def profile(self):
        print("Professor profile")

p = Professor()

p.profile()
p.teach()
p.research()
p.info()

print(Professor.mro())