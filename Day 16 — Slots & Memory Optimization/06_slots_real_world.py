"""
========================================
06_slots_real_world.py
========================================
Real-world Usage:

✔ Useful in large-scale systems
✔ Reduces memory usage for millions of objects
"""

class User:
    __slots__ = ["id", "username", "email"]

    def __init__(self, id, username, email):
        self.id = id
        self.username = username
        self.email = email

u = User(1, "monjur", "monjur@email.com")

print(u.username)