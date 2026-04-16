"""
========================================
06_ecommerce_service.py
========================================
Service Layer:

✔ Business logic controller
"""

from 03_cart_system import Cart
from 04_order_system import Order

class ECommerceService:
    def create_order(self, user, cart):
        order = Order(user, cart)
        order.confirm_order()
        return order