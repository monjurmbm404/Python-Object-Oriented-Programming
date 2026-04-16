"""
========================================
02_kiss_principle.py
========================================
KISS → Keep It Simple, Stupid

✔ Avoid unnecessary complexity
✔ Simple code = readable + maintainable
"""

# ❌ BAD (overcomplicated)
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

# ✔ GOOD (simple)
def is_even_simple(num):
    return num % 2 == 0

print(is_even_simple(10))