# 🐍 Python OOP – Day 13: Class Methods & Static Methods

---

## 📌 Overview

In this day, you will learn **special types of methods** in Python OOP:

- ⚙️ **Class Methods**
- 🧩 **Static Methods**

These methods help you write **cleaner, smarter, and more reusable code**.

---

## 💡 Why This is Important?

Normal methods use `self` and work with objects.

But sometimes you need:

- 🔹 To work with the **class itself**
- 🔹 To create **utility/helper functions**
- 🔹 To build objects in different ways

That’s where **`@classmethod`** and **`@staticmethod`** come in 🚀

---

# ⚙️ 01. Class Method (`@classmethod`)

## 📁 01_classmethod_basics.py

### 📘 Explanation:

A class method:

- 🔹 Works with the **class**, not the object
- 🔹 Uses `cls` instead of `self`
- 🔹 Can modify **class variables**

### 🧠 Example:

```python
class Student:
    school = "ABC School"  # class variable

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school(cls, new_name):
        cls.school = new_name  # modify class variable

print(Student.school)

Student.change_school("XYZ School")

print(Student.school)
```

### 🧠 Key Points:

- 🔹 Affects all objects
- 🔹 Used for class-level operations

---

# 👥 02. Class Method with Objects

## 📁 02_classmethod_with_objects.py

### 📘 Explanation:

- Class methods can be called using:
  - Class
  - Object

### 🧠 Example:

```python
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

c1 = Counter()
c2 = Counter()

print(Counter.get_count())
print(c1.get_count())
```

### 🧠 Key Points:

- 🔹 Tracks shared data
- 🔹 Works same via class or object

---

# 🧩 03. Static Method (`@staticmethod`)

## 📁 03_staticmethod_basics.py

### 📘 Explanation:

A static method:

- 🔹 Does NOT use `self` or `cls`
- 🔹 Works like a normal function inside a class
- 🔹 Used for **utility functions**

### 🧠 Example:

```python
class MathUtils:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def square(x):
        return x * x

print(MathUtils.add(5, 3))
print(MathUtils.square(4))
```

### 🧠 Key Points:

- 🔹 No access to class or object
- 🔹 Just logical/helper functions

---

# ⚖️ 04. Class Method vs Static Method

## 📁 04_class_vs_static_method.py

### 📘 Explanation:

| Feature | Class Method | Static Method    |
| ------- | ------------ | ---------------- |
| Uses    | `cls`        | Nothing          |
| Access  | Class data   | No data access   |
| Purpose | Modify class | Utility function |

### 🧠 Example:

```python
class Demo:
    value = 10

    @classmethod
    def show_class(cls):
        print("Class value:", cls.value)

    @staticmethod
    def show_static():
        print("Static method")

Demo.show_class()
Demo.show_static()
```

---

# 🏭 05. Factory Method (Very Important)

## 📁 05_factory_method.py

### 📘 Explanation:

Factory method:

- 🔹 Special type of class method
- 🔹 Creates object from different input format

### 🧠 Example:

```python
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    @classmethod
    def from_string(cls, data):
        username, email = data.split("-")
        return cls(username, email)

u1 = User.from_string("monjur-monjur@email.com")

print(u1.username)
print(u1.email)
```

### 🧠 Key Points:

- 🔹 Alternative constructor
- 🔹 Very useful in real-world apps

---

# 🌍 06. Real-World Factory Example

## 📁 06_real_world_factory.py

### 📘 Explanation:

- Create objects from structured data (like API response)

### 🧠 Example:

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = int(price)

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["price"])

data = {"name": "Laptop", "price": "50000"}

p = Product.from_dict(data)

print(p.name, p.price)
```

---

# 🔄 07. Combined Example

## 📁 07_combined_example.py

### 📘 Explanation:

- Using both classmethod + staticmethod together

### 🧠 Example:

```python
class Account:
    bank_name = "ABC Bank"

    def __init__(self, balance):
        self.balance = balance

    @classmethod
    def change_bank(cls, name):
        cls.bank_name = name

    @staticmethod
    def is_valid_amount(amount):
        return amount > 0

print(Account.is_valid_amount(100))
print(Account.is_valid_amount(-50))

Account.change_bank("XYZ Bank")
print(Account.bank_name)
```

---

# 🧪 Practice Section

---

## 📁 08_practice_student_system.py

### 📘 Task:

- 🔹 Change school using class method
- 🔹 Check pass/fail using static method

---

## 📁 09_practice_order_factory.py

### 📘 Task:

- 🔹 Create object from list
- 🔹 Use factory method

---

# 🎯 Day 13 Summary

## ⚙️ Class Method

- 🔹 Works with class (`cls`)
- 🔹 Modifies class data
- 🔹 Shared across all objects

## 🧩 Static Method

- 🔹 No `self` or `cls`
- 🔹 Utility/helper functions
- 🔹 Independent logic

## 🏭 Factory Method

- 🔹 Alternative constructor
- 🔹 Creates objects from different formats

## 🧠 Design Understanding

- 🔹 When to use class-level logic
- 🔹 When to use utility functions
- 🔹 Writing clean and scalable code

---

# Author

**Engr. Md Monjur Bakth Mazumder**

🎓 Diploma in Computer Science and Technology — [Moulvibazar Polytechnic Institute](https://mpi.moulvibazar.gov.bd/)  
🎓 BSc in Computer Science & Engineering (CSE) (Ongoing) — [Sylhet International University](https://siu.edu.bd/)

📧 Email: monjurmbm404@gmail.com

### ⭐ If you find this helpful, don’t forget to **star** the repository!
