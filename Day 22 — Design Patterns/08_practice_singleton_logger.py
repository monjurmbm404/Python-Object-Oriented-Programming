"""
========================================
08_practice_singleton_logger.py
========================================
Practice: Logger Singleton
"""

class Logger:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def log(self, msg):
        print("LOG:", msg)

l1 = Logger()
l2 = Logger()

l1.log("Hello")

print(l1 is l2)