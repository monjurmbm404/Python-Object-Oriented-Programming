"""
========================================
05_iterator_vs_loop.py
========================================
Iterator vs Loop:

✔ Loop uses iterator internally
✔ Iterator gives full control
"""

nums = [10, 20, 30]

# for loop (automatic iterator)
for n in nums:
    print(n)

# manual iterator
it = iter(nums)

print(next(it))
print(next(it))