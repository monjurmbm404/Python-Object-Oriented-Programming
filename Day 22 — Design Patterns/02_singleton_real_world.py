"""
========================================
02_singleton_real_world.py
========================================
Real-world Singleton:

✔ One database connection shared
"""

class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Connecting to database...")
            cls._instance = super().__new__(cls)
        return cls._instance

db1 = Database()
db2 = Database()

print(db1 is db2)  # True