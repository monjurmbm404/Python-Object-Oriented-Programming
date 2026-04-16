"""
========================================
02_public_protected_private.py
========================================
Access Levels:

✔ Public    → accessible everywhere
✔ Protected → internal use (_var)
✔ Private   → restricted (__var)
"""

class Demo:
    def __init__(self):
        self.public = "I am Public"
        self._protected = "I am Protected"
        self.__private = "I am Private"

obj = Demo()

print(obj.public)
print(obj._protected)

# print(obj.__private) ❌ Not directly accessible