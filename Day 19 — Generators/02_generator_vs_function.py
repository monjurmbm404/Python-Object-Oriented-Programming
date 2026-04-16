"""
========================================
02_generator_vs_function.py
========================================
Generator vs Normal Function:

✔ return → ends function
✔ yield → pauses function
"""

# Normal function (returns all at once)
def normal_function():
    return [1, 2, 3]

# Generator function (one by one)
def generator_function():
    yield 1
    yield 2
    yield 3

print(normal_function())

gen = generator_function()

for value in gen:
    print(value)