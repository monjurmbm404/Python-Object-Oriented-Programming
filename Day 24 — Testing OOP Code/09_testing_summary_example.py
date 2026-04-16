"""
========================================
09_testing_summary_example.py
========================================
Combined Testing Example:
"""

class Cart:
    def total(self, prices):
        return sum(prices)

def test_cart():
    cart = Cart()
    assert cart.total([100, 200, 300]) == 600
    assert cart.total([]) == 0  # edge case

test_cart()
print("Cart tests passed")