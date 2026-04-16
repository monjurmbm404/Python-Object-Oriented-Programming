"""
========================================
03_iterator_internal_working.py
========================================
Internal Working:

✔ for loop uses iter() + next()
"""

class Counter:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 3:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration

c = Counter()

it = iter(c)

print(next(it))
print(next(it))
print(next(it))