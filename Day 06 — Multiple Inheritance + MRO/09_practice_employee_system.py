"""
========================================
09_practice_employee_system.py
========================================
Practice: Employee System
"""

class Worker:
    def work(self):
        print("Working")

class Developer:
    def code(self):
        print("Writing code")

class Designer:
    def design(self):
        print("Designing UI")

class Freelancer(Worker, Developer, Designer):
    pass

f = Freelancer()

f.work()
f.code()
f.design()

print(Freelancer.mro())