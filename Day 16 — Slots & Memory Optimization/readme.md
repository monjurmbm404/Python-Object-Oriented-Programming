# 🐍 Python OOP – Day 16: `__slots__` & Memory Optimization

---

## 📌 Overview

💡 **What is `__slots__`?**

In Python, every object normally stores its attributes inside a **dictionary (`__dict__`)**.
This makes objects flexible but also increases **memory usage**.

👉 `__slots__` is a special feature that:

- Removes `__dict__`
- Restricts allowed attributes
- Makes objects **faster and memory efficient**

---

## 🎯 Why use `__slots__`?

- Reduces memory usage
- Improves performance
- Prevents adding unwanted attributes
- Useful in large-scale systems (millions of objects)

---

# 📁 01_without_slots.py

```python id="d1"
"""
Normal Python Object (No __slots__)
"""

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s = Student("Monjur", 22)

print(s.__dict__)
```

### 💡 Explanation:

- Python stores attributes in a dictionary
- Flexible but memory-heavy
- Every object has extra overhead

---

# 📁 02_with_slots.py

```python id="d2"
"""
Using __slots__
"""

class Student:
    __slots__ = ["name", "age"]

    def __init__(self, name, age):
        self.name = name
        self.age = age

s = Student("Monjur", 22)

print(s.name)
print(s.age)
```

### 💡 Explanation:

- No `__dict__` created
- Only allowed attributes: `name`, `age`
- Faster and memory optimized

---

# 📁 03_slots_memory_comparison.py

```python id="d3"
import sys

class NormalStudent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class SlottedStudent:
    __slots__ = ["name", "age"]

    def __init__(self, name, age):
        self.name = name
        self.age = age

n = NormalStudent("A", 20)
s = SlottedStudent("A", 20)

print(sys.getsizeof(n))
print(sys.getsizeof(s))
```

### 💡 Explanation:

- Normal class → uses more memory
- Slotted class → compact memory layout
- Useful for high-performance apps

---

# 📁 04_slots_attribute_restriction.py

```python id="d4"
class Product:
    __slots__ = ["name", "price"]

    def __init__(self, name, price):
        self.name = name
        self.price = price

p = Product("Laptop", 50000)

print(p.name)

# p.category = "Electronics" ❌ not allowed
```

### 💡 Explanation:

- You cannot add new attributes dynamically
- Prevents bugs and unwanted data

---

# 📁 05_slots_inheritance.py

```python id="d5"
class Animal:
    __slots__ = ["name"]

    def __init__(self, name):
        self.name = name

class Dog(Animal):
    __slots__ = ["breed"]

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

d = Dog("Tommy", "Labrador")

print(d.name)
print(d.breed)
```

### 💡 Explanation:

- Each class must define its own `__slots__`
- Helps maintain memory optimization in inheritance

---

# 📁 06_slots_real_world.py

```python id="d6"
class User:
    __slots__ = ["id", "username", "email"]

    def __init__(self, id, username, email):
        self.id = id
        self.username = username
        self.email = email

u = User(1, "monjur", "mail@example.com")

print(u.username)
```

### 💡 Explanation:

- Real-world backend systems use this pattern
- Saves memory when handling millions of users

---

# 📁 07_slots_vs_normal.py

```python id="d7"
class Normal:
    def __init__(self):
        self.a = 10
        self.b = 20

class Slotted:
    __slots__ = ["a", "b"]

    def __init__(self):
        self.a = 10
        self.b = 20

n = Normal()

print(n.__dict__)
```

### 💡 Explanation:

- Normal class → flexible but heavy
- Slotted class → strict but optimized

---

# 📁 08_practice_bank_system.py

```python id="d8"
class BankAccount:
    __slots__ = ["owner", "balance"]

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

acc = BankAccount("Monjur", 1000)
acc.deposit(500)

print(acc.owner, acc.balance)
```

### 💡 Explanation:

- Efficient object design for banking systems
- Prevents accidental attribute creation

---

# 📁 09_practice_large_system.py

```python id="d9"
class Product:
    __slots__ = ["name", "price"]

    def __init__(self, name, price):
        self.name = name
        self.price = price

products = [
    Product("Laptop", 50000),
    Product("Phone", 20000)
]

for p in products:
    print(p.name, p.price)
```

### 💡 Explanation:

- Optimized for large product lists
- Used in e-commerce backend systems

---

# 🎯 Day 16 Summary

Today you learned:

- 🧠 How Python stores objects internally (`__dict__`)
- ⚙️ What `__slots__` is and why it matters
- 🚀 Memory optimization techniques
- 🔒 Attribute restriction for safety
- 🏗 Real-world usage in large systems
- ⚖ Difference between normal vs slotted classes

---

# Author

**Engr. Md Monjur Bakth Mazumder**

🎓 Diploma in Computer Science and Technology — [Moulvibazar Polytechnic Institute](https://mpi.moulvibazar.gov.bd/)  
🎓 BSc in Computer Science & Engineering (CSE) (Ongoing) — [Sylhet International University](https://siu.edu.bd/)

📧 Email: monjurmbm404@gmail.com

### ⭐ If you find this helpful, don’t forget to **star** the repository!
