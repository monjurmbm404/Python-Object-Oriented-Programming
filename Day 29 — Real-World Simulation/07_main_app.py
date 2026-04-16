"""
========================================
07_main_app.py
========================================
Main Application:

✔ Connect everything
"""

from 01_user_model import User
from 02_product_model import Product
from 03_cart_system import Cart
from 06_ecommerce_service import ECommerceService

# Create user
user = User(1, "Monjur")

# Create products
p1 = Product(101, "Laptop", 50000)
p2 = Product(102, "Phone", 20000)

# Create cart
cart = Cart()
cart.add_item(p1)
cart.add_item(p2)

# Show cart
print("Cart Items:")
cart.show_cart()

print("\nTotal:", cart.total_price())

# Create order
service = ECommerceService()
order = service.create_order(user, cart)

print("\n", order)