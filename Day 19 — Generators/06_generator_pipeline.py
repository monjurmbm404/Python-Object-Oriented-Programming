"""
========================================
06_generator_pipeline.py
========================================
Pipeline Processing:

✔ Chain multiple generators
"""

def read_data():
    for i in range(5):
        yield i

def square(data):
    for i in data:
        yield i * i

def filter_even(data):
    for i in data:
        if i % 2 == 0:
            yield i

data = read_data()
squared = square(data)
filtered = filter_even(squared)

for value in filtered:
    print(value)