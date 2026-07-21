# 🐍 Python OOP – Day 29 — Real-World Simulation

## 📌 Overview

💡 What is a Real-World Backend Simulation in OOP?

A real-world backend simulation means designing your program like a real production system (like Amazon or Daraz backend).

Instead of writing random classes, we organize the system into:

- Users (who use the system)
- Products (what we sell)
- Cart (temporary selection)
- Orders (final purchase)
- Services (business logic layer)

This is called **layered architecture**, and it is used in real backend systems.

---

# 📁 01_user_model.py

```python id="oop29a1"
"""
========================================
User Model
========================================

✔ Represents a system user
✔ Only stores data (no business logic)
"""

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def __str__(self):
        return f"{self.user_id} - {self.name}"
```

---

# 📁 02_product_model.py

```python id="oop29a2"
"""
========================================
Product Model
========================================

✔ Represents a product in system
✔ Basic data structure
"""

class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

    def __str__(self):
        return f"{self.name} - {self.price}"
```

---

# 📁 03_cart_system.py

```python id="oop29a3"
"""
========================================
Cart System
========================================

✔ Cart contains products (Composition)
✔ Handles shopping logic
"""

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)

    def remove_item(self, product):
        self.items.remove(product)

    def total_price(self):
        return sum(item.get_price() for item in self.items)

    def show_cart(self):
        for item in self.items:
            print(item)
```

---

# 📁 04_order_system.py

```python id="oop29a4"
"""
========================================
Order System
========================================

✔ Converts cart into final order
✔ Represents transaction
"""

class Order:
    def __init__(self, user, cart):
        self.user = user
        self.cart = cart
        self.total = cart.total_price()
        self.status = "PENDING"

    def confirm_order(self):
        self.status = "CONFIRMED"

    def __str__(self):
        return f"{self.user.name} | Total: {self.total} | Status: {self.status}"
```

---

# 📁 05_inventory_system.py

```python id="oop29a5"
"""
========================================
Inventory System
========================================

✔ Manages product stock availability
"""

class Inventory:
    def __init__(self):
        self.stock = {}

    def add_product(self, product, quantity):
        self.stock[product.product_id] = {
            "product": product,
            "qty": quantity
        }

    def is_available(self, product_id):
        return product_id in self.stock and self.stock[product_id]["qty"] > 0
```

---

# 📁 06_ecommerce_service.py

```python id="oop29a6"
"""
========================================
Service Layer (Business Logic)
========================================

✔ Handles order creation logic
✔ Keeps system clean and organized
"""

from 04_order_system import Order

class ECommerceService:
    def create_order(self, user, cart):
        order = Order(user, cart)
        order.confirm_order()
        return order
```

---

# 📁 07_main_app.py

```python id="oop29a7"
"""
========================================
Main Application
========================================

✔ Entry point of system
✔ Connects all modules together
"""

from 01_user_model import User
from 02_product_model import Product
from 03_cart_system import Cart
from 06_ecommerce_service import ECommerceService

# Create user
user = User(1, "Monjur")

# Create products
laptop = Product(101, "Laptop", 50000)
phone = Product(102, "Phone", 20000)

# Create cart
cart = Cart()
cart.add_item(laptop)
cart.add_item(phone)

# Show cart
print("Cart Items:")
cart.show_cart()

print("\nTotal Price:", cart.total_price())

# Create order
service = ECommerceService()
order = service.create_order(user, cart)

print("\nOrder Details:")
print(order)
```

---

# 📁 08_architecture_view.py

```python id="oop29a8"
"""
========================================
Architecture Overview
========================================

System Flow:

User → Cart → Order → Service Layer

✔ Clean separation:
- Models (data)
- Services (logic)
- Main (execution)
"""

print("Backend architecture thinking activated 🚀")
```

---

# 📁 09_real_world_thinking.py

```python id="oop29a9"
"""
========================================
Real World Thinking
========================================

✔ Each class = real-world entity
✔ System design > coding
✔ Think like backend engineer
"""

print("You are now thinking like a software engineer 🚀")
```

---

# 🧠 WHAT YOU LEARNED

## 🏗️ 1. Backend Architecture Thinking

- System divided into layers
- Each module has a responsibility

---

## 🧩 2. Real World Mapping

- User → real user
- Product → real item
- Cart → shopping basket
- Order → transaction

---

## 🔗 3. Composition

- Cart contains products
- Order contains cart

---

## ⚙️ 4. Service Layer

- Business logic separated from models
- Cleaner and scalable design

---

## 🚀 5. Engineering Mindset

- Think system first, code later
- Structure > features

---

# 🏁 Day 29 Summary

- learned real-world backend system design
- built modular e-commerce architecture
- practiced layered OOP design
- understood service-based architecture
- developed engineering-level thinking

---


# Author

## **Engr. Md Monjur Bakth Mazumder**

🎓 **Secondary School Certificate (SSC) from [Shah Helal High School](https://www.shahhelalhs.edu.bd/)**

🎓 **Diploma in Computer Science and Technology from [Moulvibazar Polytechnic Institute (MPI)](https://mpi.moulvibazar.gov.bd/)**

🎓 **BSc in Computer Science & Engineering (CSE)** _(Ongoing)_ **at [Sylhet International University (SIU)](https://siu.edu.bd/)**

📧 **Email:** monjurmbm404@gmail.com

---

## ⭐ Support the Project

If you found this repository helpful, please consider giving it a **⭐ Star**. It helps others discover the project and motivates future development.

---

## 🌐 Connect with Me

| Platform       | Link                                        |
| -------------- | ------------------------------------------- |
| 💻 GitHub      | https://github.com/monjurmbm404             |
| 💼 LinkedIn    | https://linkedin.com/in/monjurmbm404        |
| 🧩 LeetCode    | https://leetcode.com/u/monjurmbm404         |
| ⚔️ Codeforces  | https://codeforces.com/profile/monjurmbm404 |
| 🍽️ CodeChef    | https://www.codechef.com/users/monjurmbm404 |
| 🏆 VJudge      | https://vjudge.net/user/monjurmbm404        |
| 📘 Facebook    | https://www.facebook.com/monjurmbm404       |
| 🐦 X (Twitter) | https://x.com/monjurmbm404                  |
| ▶️ YouTube     | https://youtube.com/@monjurmbm404           |
| ✍️ Medium      | https://medium.com/@monjurmbm404            |

