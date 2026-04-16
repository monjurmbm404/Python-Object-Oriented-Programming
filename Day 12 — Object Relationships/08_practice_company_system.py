"""
========================================
08_practice_company_system.py
========================================
Practice: Company System
"""

class Employee:
    def __init__(self, name):
        self.name = name

class Company:
    def __init__(self):
        self.employees = []  # aggregation

    def hire(self, emp):
        self.employees.append(emp)

    def show(self):
        for e in self.employees:
            print(e.name)

e1 = Employee("A")
e2 = Employee("B")

comp = Company()

comp.hire(e1)
comp.hire(e2)

comp.show()