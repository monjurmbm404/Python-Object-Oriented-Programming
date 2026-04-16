"""
========================================
09_practice_safe_system.py
========================================
Practice: Safe System Design
"""

class SafeSystem:
    def __init__(self, data):
        self.data = data

    def get_item(self, index):
        try:
            return self.data[index]
        except IndexError:
            return "Invalid index"

system = SafeSystem([10, 20, 30])

print(system.get_item(1))
print(system.get_item(10))