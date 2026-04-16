"""
========================================
09_practice_composition_system.py
========================================
Practice: Composition System
"""

class CPU:
    def process(self):
        print("Processing...")

class Computer:
    def __init__(self):
        self.cpu = CPU()  # strong composition

    def run(self):
        self.cpu.process()
        print("Computer running")

pc = Computer()
pc.run()