from models.user import User
from models.product import Product
from services.cart_service import Cart
from services.order_service import Order

# User
user = User(1, "Monjur")

# Products
p1 = Product(101, "Laptop", 50000)
p2 = Product(102, "Phone", 20000)

# Cart
cart = Cart()
cart.add(p1)
cart.add(p2)

print("Total:", cart.total())

# Order
order = Order(user, cart)
order.save()

print("Order saved successfully 🚀")