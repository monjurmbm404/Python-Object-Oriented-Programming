"""
========================================
09_practice_order_factory.py
========================================
Practice: Order Factory
"""

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    @classmethod
    def from_list(cls, data):
        return cls(data[0], data[1])

order_data = ["Book", 500]

o = Order.from_list(order_data)

print(o.item, o.price)