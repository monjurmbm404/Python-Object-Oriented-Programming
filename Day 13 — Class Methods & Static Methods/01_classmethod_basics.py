"""
========================================
01_classmethod_basics.py
========================================
@classmethod:

✔ Works with class, not instance
✔ Uses 'cls' instead of 'self'
✔ Can modify class-level data
"""

class Student:
    school = "ABC School"  # class variable

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school(cls, new_name):
        cls.school = new_name  # modifies class variable

# Before change
print(Student.school)

# Call class method
Student.change_school("XYZ School")

# After change
print(Student.school)