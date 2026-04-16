"""
========================================
01_bad_code_example.py
========================================
❌ BAD CODE:

Problems:
- No structure
- Repeated logic
- Hard to maintain
"""

class User:
    def __init__(self, n, e, b):
        self.n = n
        self.e = e
        self.b = b

    def show(self):
        print(self.n, self.e, self.b)

    def update_balance(self, x):
        self.b += x
        print("Updated:", self.b)