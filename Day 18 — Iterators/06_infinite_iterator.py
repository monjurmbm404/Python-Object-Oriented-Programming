"""
========================================
06_infinite_iterator.py
========================================
Infinite Iterator:

✔ Generates values endlessly (careful!)
"""

class InfiniteCounter:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        value = self.num
        self.num += 1
        return value  # no StopIteration → infinite

counter = InfiniteCounter()

it = iter(counter)

print(next(it))
print(next(it))
print(next(it))