# 🐍 Python OOP – Day 26 — Mini Project 2 - E-commerce Cart System

---

## 📌 Overview

💡 What is an E-commerce Cart System in OOP?

An E-commerce Cart System is a real-world application where users can add products, calculate total prices, and manage items inside a shopping cart.

In this project, you will learn:

- Composition (Cart HAS Products)
- Polymorphism (same method, different behavior)
- Inheritance (Product hierarchy)
- Clean and scalable OOP design

👉 Simple idea:

- Product = base item
- Physical Product = item + shipping cost
- Digital Product = item only
- Cart = container holding products

---

## 📁 01_product_base.py

💡 Base class for all products

- Stores common product data
- Provides basic methods

```python id="p1a8kd"
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

    def display(self):
        return f"{self.name} - {self.price}"
```

---

## 📁 02_physical_product.py

💡 Physical products include shipping cost

- Example: Laptop, Mobile
- Overrides price calculation

```python id="x9k3pd"
from 01_product_base import Product

class PhysicalProduct(Product):
    def __init__(self, name, price, shipping_cost):
        super().__init__(name, price)
        self.shipping_cost = shipping_cost

    def get_price(self):
        return self.price + self.shipping_cost
```

---

## 📁 03_digital_product.py

💡 Digital products have no shipping cost

- Example: E-book, Online course
- Same method name → different behavior (polymorphism)

```python id="d8m2qp"
from 01_product_base import Product

class DigitalProduct(Product):
    def get_price(self):
        return self.price
```

---

## 📁 04_cart_composition.py

💡 Cart uses composition (HAS-A relationship)

- Cart contains products
- Not inheritance → better design

```python id="c3n9kd"
class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)

    def remove_product(self, product):
        self.items.remove(product)

    def total_price(self):
        total = 0
        for item in self.items:
            total += item.get_price()
        return total

    def show_items(self):
        for item in self.items:
            print(item.display())
```

---

## 📁 05_main_system.py

💡 Main system that runs everything

- Creates products
- Adds to cart
- Calculates total

```python id="m8p4kd"
from 02_physical_product import PhysicalProduct
from 03_digital_product import DigitalProduct
from 04_cart_composition import Cart

laptop = PhysicalProduct("Laptop", 50000, 500)
book = DigitalProduct("Python Book", 500)

cart = Cart()

cart.add_product(laptop)
cart.add_product(book)

print("Items in cart:")
cart.show_items()

print("\nTotal Price:", cart.total_price())
```

---

## 📁 06_polymorphism_demo.py

💡 Same method behaves differently in different classes

```python id="p9m2kd"
from 02_physical_product import PhysicalProduct
from 03_digital_product import DigitalProduct

products = [
    PhysicalProduct("Phone", 20000, 300),
    DigitalProduct("Course", 1000)
]

for p in products:
    print(p.name, "->", p.get_price())
```

---

## 📁 07_cart_extension.py

💡 System is easily extendable

- You can add new product types without changing old code

```python id="k2m9pd"
class SubscriptionProduct:
    def __init__(self, name, monthly_fee):
        self.name = name
        self.monthly_fee = monthly_fee

    def get_price(self):
        return self.monthly_fee

    def display(self):
        return f"{self.name} Subscription - {self.monthly_fee}"
```

---

## 📁 08_real_world_design.py

💡 Real-world cart logic simplified

```python id="r8k3md"
class Cart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def checkout(self):
        return sum(item.get_price() for item in self.items)
```

---

## 🎯 Day 26 Summary

- Learned Composition (Cart HAS Products)
- Practiced Polymorphism (same method, different behavior)
- Used Inheritance for product types
- Designed a real-world e-commerce system
- Built a scalable and extensible architecture
- Understood how real online shopping carts work

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

