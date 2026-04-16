"""
========================================
07_exception_with_validation.py
========================================
Validation with Exceptions:

✔ Ensure data correctness
"""

class User:
    def __init__(self, username, age):
        if len(username) < 3:
            raise ValueError("Username too short")
        if age < 0:
            raise ValueError("Invalid age")

        self.username = username
        self.age = age

try:
    u = User("ab", 20)
except ValueError as e:
    print("Validation Error:", e)