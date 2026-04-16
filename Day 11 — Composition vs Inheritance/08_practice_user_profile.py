"""
========================================
08_practice_user_profile.py
========================================
Practice: User Profile System
"""

class Address:
    def __init__(self, city, country):
        self.city = city
        self.country = country

class User:
    def __init__(self, name, address):
        self.name = name
        self.address = address  # composition

    def show(self):
        print(self.name)
        print(self.address.city, self.address.country)

addr = Address("Sylhet", "Bangladesh")
user = User("Monjur", addr)

user.show()