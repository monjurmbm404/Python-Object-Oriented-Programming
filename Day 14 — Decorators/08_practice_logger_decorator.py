"""
========================================
08_practice_logger_decorator.py
========================================
Practice: Logger Decorator
"""

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

class App:
    @logger
    def run(self):
        print("App is running")

a = App()
a.run()