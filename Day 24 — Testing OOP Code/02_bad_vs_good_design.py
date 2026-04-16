"""
========================================
02_bad_vs_good_design.py
========================================
Bad vs Good Design:

❌ BAD: Hard to test
✔ GOOD: Easy to test
"""

# ❌ BAD (hard dependency)
class Payment:
    def process(self):
        print("Connecting to real bank...")
        return True

# ✔ GOOD (testable)
class Payment:
    def __init__(self, gateway):
        self.gateway = gateway

    def process(self):
        return self.gateway.pay()