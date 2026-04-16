"""
========================================
04_custom_logic_comparisons.py
========================================
Custom Logic Comparisons:

✔ Compare based on custom rules
"""

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __gt__(self, other):
        return self.marks > other.marks

    def __eq__(self, other):
        return self.marks == other.marks

s1 = Student("A", 85)
s2 = Student("B", 90)

print(s1 > s2)
print(s1 == s2)