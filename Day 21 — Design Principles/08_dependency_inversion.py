"""
========================================
08_dependency_inversion.py
========================================
Dependency Inversion Principle:

✔ High-level should not depend on low-level
✔ Use abstraction
"""

class Database:
    def connect(self):
        print("Connected to DB")

class App:
    def __init__(self, db):
        self.db = db  # injected dependency

    def start(self):
        self.db.connect()

db = Database()
app = App(db)

app.start()