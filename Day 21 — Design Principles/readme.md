# 🐍 Python OOP – Day 21 — Design Principles

---

## 📌 Overview

In this day, you learn how to write **clean, maintainable, and professional-level code** using important design principles like **DRY, KISS, and SOLID**.

---

## 💡 What is Design Principles?

Design principles are **rules or best practices** that help developers write:

* 🧩 Clean code
* 🔄 Reusable code
* 🛠 Easy-to-maintain systems
* 📈 Scalable applications

Instead of just making code work, these principles help you make code **better and professional**.

---

## 📁 01_dry_principle.py

### 💡 DRY → Don't Repeat Yourself

* 🔁 Avoid repeating the same logic
* ♻️ Reuse code using functions or classes
* 🧼 Makes code cleaner and easier to update

```python
# ❌ BAD (repetition)
def area_circle(radius):
    return 3.14 * radius * radius

def area_sphere(radius):
    return 4 * 3.14 * radius * radius  # repeated logic

# ✅ GOOD (reuse)
def circle_area(radius):
    return 3.14 * radius * radius

def sphere_area(radius):
    return 4 * circle_area(radius)

print(circle_area(5))
print(sphere_area(5))
```

---

## 📁 02_kiss_principle.py

### 💡 KISS → Keep It Simple, Stupid

* ✂️ Avoid unnecessary complexity
* 📖 Simple code = easy to read
* ⚡ Faster to debug and maintain

```python
# ❌ BAD (complex)
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

# ✅ GOOD (simple)
def is_even_simple(num):
    return num % 2 == 0

print(is_even_simple(10))
```

---

## 📁 03_solid_intro.py

### 💡 SOLID Principles (Overview)

* 🧩 S → Single Responsibility
* 🔓 O → Open/Closed
* 🔄 L → Liskov Substitution
* 🧱 I → Interface Segregation
* 🔗 D → Dependency Inversion

👉 These are **advanced design rules** for building scalable systems.

```python
# Concept only (no code here)
```

---

## 📁 04_single_responsibility.py

### 💡 SRP → Single Responsibility Principle

* 🎯 One class = one job
* 🧠 Easier to understand and maintain

```python
# ❌ BAD (multiple jobs)
class Report:
    def generate(self):
        print("Generating report")

    def save(self):
        print("Saving report")

# ✅ GOOD (separate responsibilities)
class ReportGenerator:
    def generate(self):
        print("Generating report")

class ReportSaver:
    def save(self):
        print("Saving report")

rg = ReportGenerator()
rs = ReportSaver()

rg.generate()
rs.save()
```

---

## 📁 05_open_closed.py

### 💡 OCP → Open/Closed Principle

* ➕ Add new features without changing existing code
* 🧱 Extend instead of modifying

```python
class Discount:
    def apply(self, price):
        return price

class PercentageDiscount(Discount):
    def apply(self, price):
        return price * 0.9

class FixedDiscount(Discount):
    def apply(self, price):
        return price - 100

d1 = PercentageDiscount()
d2 = FixedDiscount()

print(d1.apply(1000))
print(d2.apply(1000))
```

---

## 📁 06_liskov_substitution.py

### 💡 LSP → Liskov Substitution Principle

* 🔄 Child class should behave like parent
* ❌ Avoid incorrect inheritance

```python
class Bird:
    def fly(self):
        print("Flying")

class Sparrow(Bird):
    pass

# ❌ Problem: Penguin can't fly
class Penguin:
    def swim(self):
        print("Swimming")
```

---

## 📁 07_interface_segregation.py

### 💡 ISP → Interface Segregation Principle

* ✂️ Avoid forcing unnecessary methods
* 🧩 Use smaller, specific interfaces

```python
# ❌ BAD
class Worker:
    def work(self):
        pass

    def eat(self):
        pass

# ✅ GOOD
class Workable:
    def work(self):
        pass

class Eatable:
    def eat(self):
        pass
```

---

## 📁 08_dependency_inversion.py

### 💡 DIP → Dependency Inversion Principle

* 🔗 High-level code should not depend on low-level code
* 🧠 Use abstraction (dependency injection)

```python
class Database:
    def connect(self):
        print("Connected to DB")

class App:
    def __init__(self, db):
        self.db = db  # injected dependency

    def start(self):
        self.db.connect()

db = Database()
app = App(db)

app.start()
```

---

## 📁 09_real_world_clean_design.py

### 💡 Clean Design (All Principles Together)

* 🧩 Combines DRY + KISS + SOLID
* 🏗 Builds scalable real-world systems

```python
class Payment:
    def pay(self, amount):
        pass

class CardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} via Card")

class CashPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} via Cash")

def process_payment(method, amount):
    method.pay(amount)

process_payment(CardPayment(), 1000)
process_payment(CashPayment(), 500)
```

---

## 🎯 Day 21 Summary

* 🔁 DRY → Avoid repeating code
* ✂️ KISS → Keep things simple
* 🧩 SOLID → Build scalable systems
* 🎯 SRP → One responsibility per class
* 🔓 OCP → Extend without modifying
* 🔄 LSP → Proper inheritance behavior
* 🧱 ISP → Small and focused interfaces
* 🔗 DIP → Use dependency injection

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
