"""
========================================
03_name_mangling.py
========================================
Name Mangling:

✔ Python internally renames private variables
✔ Format: _ClassName__variable
"""

class Test:
    def __init__(self):
        self.__secret = "Hidden Data"

obj = Test()

# Access using name mangling
print(obj._Test__secret)