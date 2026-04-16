"""
========================================
02_custom_iterator_class.py
========================================
Custom Iterator Class:

✔ Implements __iter__ and __next__
✔ Controls iteration manually
"""

class MyNumbers:
    def __init__(self):
        self.current = 1

    def __iter__(self):
        return self  # object itself is iterator

    def __next__(self):
        if self.current <= 5:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration  # ends iteration

obj = MyNumbers()

for num in obj:
    print(num)