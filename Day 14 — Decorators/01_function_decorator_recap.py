"""
========================================
01_function_decorator_recap.py
========================================
Function Decorator Recap:

✔ A decorator wraps a function
✔ Adds extra behavior without modifying original function
"""

def my_decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()