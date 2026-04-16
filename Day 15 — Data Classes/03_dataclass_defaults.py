"""
========================================
03_dataclass_defaults.py
========================================
Default Values:

✔ You can set default values easily
"""

from dataclasses import dataclass

@dataclass
class User:
    username: str
    age: int = 18  # default value
    active: bool = True

u1 = User("Monjur")

print(u1)