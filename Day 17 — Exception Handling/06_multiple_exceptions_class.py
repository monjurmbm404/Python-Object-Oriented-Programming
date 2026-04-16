"""
========================================
06_multiple_exceptions_class.py
========================================
Multiple Exceptions:

✔ Handle different errors separately
"""

class DataProcessor:
    def process(self, data):
        try:
            number = int(data)
            result = 100 / number
            print("Result:", result)

        except ValueError:
            print("Invalid input: not a number")

        except ZeroDivisionError:
            print("Cannot divide by zero")

dp = DataProcessor()

dp.process("10")
dp.process("abc")
dp.process("0")