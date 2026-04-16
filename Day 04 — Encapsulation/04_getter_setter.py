"""
========================================
04_getter_setter.py
========================================
Getter & Setter:

✔ Used to access private variables safely
"""

class Student:
    def __init__(self):
        self.__marks = 0

    # Getter
    def get_marks(self):
        return self.__marks

    # Setter
    def set_marks(self, value):
        if value < 0:
            print("Invalid marks!")
        else:
            self.__marks = value

s = Student()

s.set_marks(85)
print("Marks:", s.get_marks())

s.set_marks(-10)  # validation