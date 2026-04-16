"""
========================================
02_composition_basics.py
========================================
Composition Basics:

✔ Build complex objects using smaller objects
✔ More flexible than inheritance
"""

class CPU:
    def process(self):
        print("Processing data")

class Computer:
    def __init__(self):
        self.cpu = CPU()  # composition

    def run(self):
        self.cpu.process()
        print("Computer running")

pc = Computer()
pc.run()