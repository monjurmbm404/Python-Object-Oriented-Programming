"""
========================================
02_single_inheritance_with_constructor.py
========================================
Constructor with Inheritance:

✔ Child class can have its own constructor
✔ Parent constructor can also be called
"""

class Person:
    def __init__(self, name):
        self.name = name
        print("Person constructor called")

class Student(Person):
    def __init__(self, name, marks):
        # Calling parent constructor
        super().__init__(name)
        self.marks = marks
        print("Student constructor called")

s = Student("Monjur", 90)

print(s.name)
print(s.marks)