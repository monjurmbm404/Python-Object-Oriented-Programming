"""
========================================
04_generator_in_class.py
========================================
Generator inside OOP:

✔ Method returns generator
"""

class NumberSeries:
    def __init__(self, limit):
        self.limit = limit

    def generate(self):
        for i in range(1, self.limit + 1):
            yield i

obj = NumberSeries(5)

for num in obj.generate():
    print(num)