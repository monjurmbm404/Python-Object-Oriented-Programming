# 🐍 Python OOP – Day 28 — Code Review & Optimization

## 📌 Overview

💡 What is Code Review & Optimization in OOP?

Code review and optimization means improving existing code to make it:

- easier to read
- easier to maintain
- easier to scale
- less repetitive (clean design)
- more professional (industry standard)

In real software development, writing code is only half the job — **refactoring (improving code)** is equally important.

---

# 📁 01_bad_code_example.py

```python
"""
❌ BAD CODE EXAMPLE

Problems:
- unclear variable names
- no structure
- mixed responsibilities
- hard to read and maintain
"""

class User:
    def __init__(self, n, e, b):
        self.n = n
        self.e = e
        self.b = b

    def show(self):
        print(self.n, self.e, self.b)

    def update_balance(self, x):
        self.b += x
        print("Updated:", self.b)
```

---

# 📁 02_refactored_user_class.py

```python
"""
✔ REFACTORED VERSION

Improvements:
- meaningful names
- clean structure
- better readability
"""

class User:
    def __init__(self, name, email, balance=0):
        self.name = name
        self.email = email
        self.balance = balance

    def display(self):
        return f"Name: {self.name}, Email: {self.email}, Balance: {self.balance}"

    def add_balance(self, amount):
        if amount > 0:
            self.balance += amount
```

---

# 📁 03_before_refactor_bank.py

```python
"""
❌ BAD DESIGN EXAMPLE

Problems:
- list used instead of object
- no structure
- not scalable
"""

class Bank:
    def __init__(self):
        self.users = []

    def add(self, name, balance):
        self.users.append([name, balance])

    def show(self):
        for u in self.users:
            print(u[0], u[1])
```

---

# 📁 04_after_refactor_bank.py

```python
"""
✔ IMPROVED DESIGN

Improvements:
- uses proper User class
- better data structure
- scalable design
"""

class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance


class Bank:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def show_users(self):
        for user in self.users:
            print(user.name, user.balance)
```

---

# 📁 05_remove_duplication.py

```python
"""
✔ DRY PRINCIPLE (Don't Repeat Yourself)
"""

# ❌ BAD
def area_square(x):
    return x * x

def area_cube_face(x):
    return x * x


# ✔ GOOD (reuse logic)
def square(x):
    return x * x

def area_square(x):
    return square(x)

def area_cube_face(x):
    return square(x)
```

---

# 📁 06_clean_method_design.py

```python
"""
✔ CLEAN METHOD DESIGN

Rule:
- One function = one responsibility
"""

class Calculator:

    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b
```

---

# 📁 07_structured_project.py

```python
"""
✔ PROPER PROJECT STRUCTURE IDEA

project/
│
├── models/
│   └── user.py
│
├── services/
│   └── bank_service.py
│
├── main.py
"""

# Each layer has its own responsibility
```

---

# 📁 08_best_practices.py

```python
"""
✔ BEST PRACTICES IN OOP

- meaningful names
- small methods
- reusable code
- separation of concerns
"""

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self, percent):
        return self.price - (self.price * percent / 100)
```

---

# 📁 09_before_after_summary.py

```python
"""
✔ BEFORE vs AFTER SUMMARY

❌ BEFORE:
- messy code
- duplication
- hard to scale

✔ AFTER:
- clean structure
- reusable logic
- easy maintenance
- professional design
"""
```

---

# 🎯 Day 28 Summary

- learned how to improve bad code into clean code
- understood refactoring techniques
- practiced DRY principle (remove duplication)
- learned clean class and method design
- understood real-world code structure
- developed professional coding mindset

---

# Author

**Engr. Md Monjur Bakth Mazumder**

🎓 Diploma in Computer Science and Technology — [Moulvibazar Polytechnic Institute](https://mpi.moulvibazar.gov.bd/)  
🎓 BSc in Computer Science & Engineering (CSE) (Ongoing) — [Sylhet International University](https://siu.edu.bd/)

📧 Email: monjurmbm404@gmail.com

### ⭐ If you find this helpful, don’t forget to **star** the repository!
