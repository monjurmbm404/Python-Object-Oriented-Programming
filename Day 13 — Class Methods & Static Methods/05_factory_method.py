"""
========================================
05_factory_method.py
========================================
Factory Method:

✔ Special class method
✔ Creates object using alternative input
"""

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    @classmethod
    def from_string(cls, data):
        # data format: "username-email"
        username, email = data.split("-")
        return cls(username, email)

# Create object using factory method
u1 = User.from_string("monjur-monjur@email.com")

print(u1.username)
print(u1.email)