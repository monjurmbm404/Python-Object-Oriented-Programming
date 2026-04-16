"""
========================================
08_real_world_testing.py
========================================
Real-world Example:

✔ Test business logic
"""

class Discount:
    def apply(self, price):
        return price * 0.9

def test_discount():
    d = Discount()
    assert d.apply(1000) == 900

test_discount()
print("Discount test passed")