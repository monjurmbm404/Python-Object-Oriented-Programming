"""
========================================
03_lazy_evaluation.py
========================================
Lazy Evaluation:

✔ Values generated only when needed
✔ Saves memory
"""

def numbers():
    for i in range(1, 6):
        print("Generating:", i)
        yield i

gen = numbers()

print("Start")

print(next(gen))
print(next(gen))