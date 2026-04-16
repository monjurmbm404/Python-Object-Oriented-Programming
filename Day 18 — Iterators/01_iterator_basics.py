"""
========================================
01_iterator_basics.py
========================================
Iterator Basics:

✔ Iterator → object that remembers state
✔ Used to traverse data one by one
✔ Uses __iter__ and __next__
"""

# Built-in iterator example
numbers = [1, 2, 3]

it = iter(numbers)  # create iterator

print(next(it))
print(next(it))
print(next(it))