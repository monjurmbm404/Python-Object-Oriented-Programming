"""
========================================
05_main_system.py
========================================
Main System:

✔ Combine everything
✔ Demonstrate polymorphism + composition
"""

from 02_physical_product import PhysicalProduct
from 03_digital_product import DigitalProduct
from 04_cart_composition import Cart

# Create products
laptop = PhysicalProduct("Laptop", 50000, 500)
book = DigitalProduct("Python Book", 500)

# Create cart
cart = Cart()

# Add products (composition)
cart.add_product(laptop)
cart.add_product(book)

# Show items
print("Items in cart:")
cart.show_items()

print("\nTotal Price:", cart.total_price())