"""
========================================
07_practice_user.py
========================================
Practice: User Class
"""

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def display(self):
        print("Username:", self.username)
        print("Email:", self.email)

# Create objects
u1 = User("monjur_dev", "monjur@email.com")
u2 = User("rahim123", "rahim@email.com")

u1.display()
u2.display()