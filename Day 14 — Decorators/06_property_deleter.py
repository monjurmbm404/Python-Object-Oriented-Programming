"""
========================================
06_property_deleter.py
========================================
@deleter:

✔ Controls deletion of attribute
"""

class User:
    def __init__(self, username):
        self._username = username

    @property
    def username(self):
        return self._username

    @username.deleter
    def username(self):
        print("Deleting username...")
        del self._username

u = User("monjur_dev")

print(u.username)

del u.username