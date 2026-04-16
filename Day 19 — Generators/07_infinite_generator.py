"""
========================================
07_infinite_generator.py
========================================
Infinite Generator:

✔ Generates endless values safely
"""

def infinite_counter():
    i = 1
    while True:
        yield i
        i += 1

gen = infinite_counter()

print(next(gen))
print(next(gen))
print(next(gen))