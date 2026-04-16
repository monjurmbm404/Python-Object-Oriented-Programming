"""
========================================
05_generator_memory_efficiency.py
========================================
Memory Efficiency:

✔ Generator does NOT store full list
✔ Saves RAM for large data
"""

def big_data():
    for i in range(1, 1000000):
        yield i

gen = big_data()

print(next(gen))
print(next(gen))