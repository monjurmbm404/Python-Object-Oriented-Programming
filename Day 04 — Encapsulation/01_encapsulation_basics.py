"""
========================================
01_encapsulation_basics.py
========================================
Encapsulation:

✔ Hides internal data of a class
✔ Controls access to variables
✔ Helps protect data from unwanted changes
"""

class Student:
    def __init__(self, name, age):
        self.name = name          # Public variable
        self._age = age           # Protected (convention)
        self.__marks = 90         # Private variable

    def show(self):
        print(self.name)
        print(self._age)
        print(self.__marks)

s1 = Student("Monjur", 22)
s1.show()