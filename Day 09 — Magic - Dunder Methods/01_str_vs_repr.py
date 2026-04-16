"""
========================================
01_str_vs_repr.py
========================================
__str__ vs __repr__:

✔ __str__ → user-friendly output (for print)
✔ __repr__ → developer/debug representation
"""

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Student: {self.name} ({self.marks})"

    def __repr__(self):
        return f"Student(name='{self.name}', marks={self.marks})"

s = Student("Monjur", 90)

print(s)        # calls __str__
print(repr(s))  # calls __repr__