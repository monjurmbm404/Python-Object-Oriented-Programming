"""
========================================
07_practice_user_security.py
========================================
Practice: User Security Example
"""

class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def check_password(self, password):
        return self.__password == password

u = User("monjur", "1234")

print(u.username)

print("Password correct?", u.check_password("1234"))