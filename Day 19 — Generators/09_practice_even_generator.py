"""
========================================
09_practice_even_generator.py
========================================
Practice: Even Number Generator
"""

def even_numbers(limit):
    for i in range(2, limit + 1, 2):
        yield i

gen = even_numbers(10)

for num in gen:
    print(num)