"""
========================================
02_decorator_with_arguments.py
========================================
Decorator with Arguments:

✔ Handles functions with parameters
"""

def logger(func):
    def wrapper(*args, **kwargs):
        print("Arguments:", args, kwargs)
        result = func(*args, **kwargs)
        print("Function executed")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

print(add(5, 3))