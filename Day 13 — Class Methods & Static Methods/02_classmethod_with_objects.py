"""
========================================
02_classmethod_with_objects.py
========================================
Class Method with Objects:

✔ Can be called using object or class
✔ Still affects class-level data
"""

class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

# Create objects
c1 = Counter()
c2 = Counter()

print(Counter.get_count())
print(c1.get_count())  # also works