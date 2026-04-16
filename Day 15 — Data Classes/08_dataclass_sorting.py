"""
========================================
08_dataclass_sorting.py
========================================
Sorting with Dataclass:

✔ Can be sorted automatically using order=True
"""

from dataclasses import dataclass

@dataclass(order=True)
class Student:
    marks: int
    name: str

s1 = Student(80, "A")
s2 = Student(90, "B")
s3 = Student(70, "C")

students = [s1, s2, s3]

students.sort()

for s in students:
    print(s)