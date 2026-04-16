"""
========================================
08_practice_number_iterator.py
========================================
Practice: Number Iterator
"""

class Numbers:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.end:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration

nums = Numbers(1, 5)

for n in nums:
    print(n)