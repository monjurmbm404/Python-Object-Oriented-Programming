"""
========================================
09_practice_even_iterator.py
========================================
Practice: Even Number Iterator
"""

class EvenNumbers:
    def __init__(self, limit):
        self.num = 2
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= self.limit:
            value = self.num
            self.num += 2
            return value
        else:
            raise StopIteration

evens = EvenNumbers(10)

for e in evens:
    print(e)