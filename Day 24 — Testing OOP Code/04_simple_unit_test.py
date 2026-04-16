"""
========================================
04_simple_unit_test.py
========================================
Simple Unit Test:

✔ Test small units (functions/classes)
"""

def multiply(a, b):
    return a * b

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(0, 5) == 0

test_multiply()

print("All tests passed")