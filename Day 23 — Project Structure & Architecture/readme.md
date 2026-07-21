# 🐍 Python OOP – Day 23 — Project Structure & Architecture

---

## 📌 Overview

In this day, you learn how to organize your code like a **real-world professional project** using proper structure and architecture.

---

## 💡 What is Project Structure & Architecture?

Project structure means **how you organize files and folders** in your project.

Architecture means **how different parts of your code work together**.

* 🧱 Clean structure = easy to understand
* 🔄 Organized code = easy to maintain
* 🚀 Good architecture = scalable system

---

## 📁 01_bad_structure_example.py

### 💡 Bad Project Structure

* ❌ Everything in one file
* 😵 Hard to read and manage
* 📉 Not scalable

```python
class User:
    def __init__(self, name):
        self.name = name

class Product:
    def __init__(self, price):
        self.price = price

class Payment:
    def pay(self):
        print("Paid")

# All logic mixed together → BAD
```

---

## 📁 02_good_structure_overview.py

### 💡 Good Project Structure

* 📁 Separate files by responsibility
* 🧩 Each part has a clear role
* 📈 Easy to scale

```
project/
│
├── main.py
├── models/
│   ├── user.py
│   ├── product.py
│
├── services/
│   ├── payment_service.py
│
├── utils/
│   ├── helpers.py
│
└── config/
    ├── settings.py
```

---

## 📁 03_models_user.py

### 💡 Model Layer (User)

* 📦 Represents data
* ❌ No business logic

```python
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.name} ({self.email})"
```

---

## 📁 04_models_product.py

### 💡 Model Layer (Product)

* 🏷 Stores product data

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
```

---

## 📁 05_services_payment.py

### 💡 Service Layer

* 🧠 Contains business logic
* 🔗 Works with models

```python
class PaymentService:
    def process_payment(self, user, amount):
        print(f"{user.name} paid {amount}")
```

---

## 📁 06_utils_helpers.py

### 💡 Utility Functions

* 🔧 Reusable helper functions
* ❌ No business logic

```python
def format_price(price):
    return f"${price}"
```

---

## 📁 07_config_settings.py

### 💡 Configuration

* ⚙ Stores settings and constants

```python
APP_NAME = "MyApp"
VERSION = "1.0"
```

---

## 📁 08_main_entry.py

### 💡 Main Entry Point

* 🔗 Connects all parts together

```python
from models.user import User
from services.payment_service import PaymentService

user = User("Monjur", "monjur@email.com")

payment = PaymentService()
payment.process_payment(user, 1000)
```

---

## 📁 09_package_init_files.py

### 💡 Package Initialization

* 📦 Makes folder a package
* 📥 Helps manage imports

```python
# models/__init__.py
from .user import User
from .product import Product
```

---

## 🎯 Day 23 Summary

* 🧱 Separate code into multiple files
* 📦 Understand modules and packages
* 🏗 Use layered architecture (models, services, utils, config)
* 🔗 Keep responsibilities clear
* 🚀 Build scalable and maintainable projects

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
