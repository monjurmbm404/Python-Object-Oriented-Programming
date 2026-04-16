"""
========================================
01_testing_mindset.py
========================================
Testing Mindset:

✔ Test behavior, not implementation
✔ Keep functions small
✔ Avoid hard dependencies
✔ Predictable output = testable code
"""

def add(a, b):
    return a + b

# Manual test
print(add(2, 3) == 5)  # True