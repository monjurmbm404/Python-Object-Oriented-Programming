"""
========================================
03_aggregation_basic.py
========================================
Aggregation:

✔ Weak "has-a" relationship
✔ Child can exist independently
✔ Example: Department has Teachers
"""

class Teacher:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, teachers):
        # Aggregation: receives external objects
        self.teachers = teachers

    def show_teachers(self):
        for t in self.teachers:
            print(t.name)

# Teachers exist independently
t1 = Teacher("A")
t2 = Teacher("B")

# Department aggregates teachers
dept = Department([t1, t2])

dept.show_teachers()