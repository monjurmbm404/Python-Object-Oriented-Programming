"""
========================================
04_polymorphism_with_functions.py
========================================
Polymorphism in Functions:

✔ Same function works with different objects
"""

class Laptop:
    def type(self):
        print("Laptop typing...")

class Mobile:
    def type(self):
        print("Mobile typing...")

def device_typing(device):
    device.type()

device_typing(Laptop())
device_typing(Mobile())