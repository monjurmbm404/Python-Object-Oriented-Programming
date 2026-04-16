"""
========================================
models/user.py
========================================
Model Layer:

✔ Represents data structure
✔ No business logic
"""

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.name} ({self.email})"