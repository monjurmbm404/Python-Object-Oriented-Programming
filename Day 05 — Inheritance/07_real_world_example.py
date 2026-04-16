"""
========================================
07_real_world_example.py
========================================
Real-world Example:

✔ Employee → Developer
✔ Inheritance used in real systems
"""

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print("Name:", self.name)
        print("Salary:", self.salary)

class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def show_details(self):
        # Reuse parent method
        super().show_details()
        print("Language:", self.language)

dev = Developer("Monjur", 50000, "Python")

dev.show_details()