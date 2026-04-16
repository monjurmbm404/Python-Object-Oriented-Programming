"""
========================================
06_edge_case_testing.py
========================================
Edge Cases:

✔ Always test unusual inputs
"""

def divide(a, b):
    if b == 0:
        return None
    return a / b

def test_divide():
    assert divide(10, 2) == 5
    assert divide(10, 0) is None  # edge case

test_divide()
print("Divide tests passed")