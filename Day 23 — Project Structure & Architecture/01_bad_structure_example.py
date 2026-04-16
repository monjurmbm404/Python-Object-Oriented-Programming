"""
========================================
01_bad_structure_example.py
========================================
❌ BAD PROJECT STRUCTURE:

✔ Everything in one file
✔ Hard to maintain
✔ Not scalable
"""

class User:
    def __init__(self, name):
        self.name = name

class Product:
    def __init__(self, price):
        self.price = price

class Payment:
    def pay(self):
        print("Paid")

# Everything mixed → BAD DESIGN