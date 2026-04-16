"""
========================================
09_practice_student_system.py
========================================
Practice: Student System using Dataclass
"""

from dataclasses import dataclass

@dataclass
class Student:
    name: str
    marks: int

    def passed(self):
        return self.marks >= 40

s1 = Student("Monjur", 85)
s2 = Student("Rahim", 30)

print(s1.passed())
print(s2.passed())