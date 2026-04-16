"""
========================================
05_open_closed.py
========================================
Open/Closed Principle:

✔ Open for extension
✔ Closed for modification
"""

class Discount:
    def apply(self, price):
        return price

class PercentageDiscount(Discount):
    def apply(self, price):
        return price * 0.9

class FixedDiscount(Discount):
    def apply(self, price):
        return price - 100

# No need to modify existing code → extend only
d1 = PercentageDiscount()
d2 = FixedDiscount()

print(d1.apply(1000))
print(d2.apply(1000))