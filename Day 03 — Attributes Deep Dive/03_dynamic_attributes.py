"""
========================================
03_dynamic_attributes.py
========================================
Dynamic Attributes:

✔ Add attributes outside class definition
✔ Python allows runtime attribute creation
"""

class User:
    def __init__(self, name):
        self.name = name

u1 = User("Monjur")

# Adding attribute dynamically
u1.age = 22
u1.email = "monjur@email.com"

print(u1.name)
print(u1.age)
print(u1.email)