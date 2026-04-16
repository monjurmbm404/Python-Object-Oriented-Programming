"""
========================================
03_method_decorator.py
========================================
Method Decorator:

✔ Works with class methods
✔ 'self' must be handled properly
"""

def log_method(func):
    def wrapper(self, *args, **kwargs):
        print(f"Calling method: {func.__name__}")
        return func(self, *args, **kwargs)
    return wrapper

class Calculator:
    @log_method
    def multiply(self, a, b):
        return a * b

c = Calculator()
print(c.multiply(4, 5))