"""
========================================
05_remove_duplication.py
========================================
DRY Principle (Refactor):

✔ Remove duplicate code
"""

# ❌ BAD
def area_square(x):
    return x * x

def area_cube_face(x):
    return x * x

# ✔ GOOD
def square(x):
    return x * x

def area_square(x):
    return square(x)

def area_cube_face(x):
    return square(x)