"""
========================================
06_dependency_injection_style.py
========================================
Dependency Injection (Advanced Composition):

✔ Pass dependency from outside
✔ Makes code flexible & testable
"""

class Database:
    def connect(self):
        print("Database connected")

class App:
    def __init__(self, db):
        self.db = db  # injected dependency

    def start(self):
        self.db.connect()
        print("App started")

db = Database()
app = App(db)

app.start()