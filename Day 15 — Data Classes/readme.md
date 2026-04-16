# 🐍 Python OOP – Day 15: Data Classes

---

## 📌 Overview

💡 **What is a Data Class?**

A **dataclass** is a special feature in Python that helps you create classes **faster and cleaner**.

Instead of writing boilerplate code like:

* `__init__`
* `__repr__`
* `__eq__`

Python automatically generates them for you.

👉 So you can focus on **data, not repetitive code**.

---

## 🎯 Why use Data Classes?

* Less code, more readability
* Auto-generated constructor (`__init__`)
* Easy object printing (`__repr__`)
* Built-in comparison (`==`) support
* Perfect for models (Student, Product, Order, etc.)

---

# 📁 01_dataclass_basic.py

```python
"""
Basic Data Class Example
"""

from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
    marks: int

s1 = Student("Monjur", 22, 90)

print(s1)
```

### 💡 Explanation:

* `@dataclass` automatically creates constructor
* You don’t need to write `__init__`
* Printing object shows readable output

---

# 📁 02_dataclass_init_auto.py

```python
from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: int

p = Product("Laptop", 50000)

print(p.name)
print(p.price)
```

### 💡 Explanation:

* Python auto-generates `__init__`
* You can directly assign values during object creation

---

# 📁 03_dataclass_defaults.py

```python
from dataclasses import dataclass

@dataclass
class User:
    username: str
    age: int = 18
    active: bool = True

u1 = User("Monjur")

print(u1)
```

### 💡 Explanation:

* You can set **default values**
* If value not provided → default is used

---

# 📁 04_dataclass_comparison.py

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

p1 = Point(1, 2)
p2 = Point(1, 2)

print(p1 == p2)
```

### 💡 Explanation:

* Dataclass auto-generates `__eq__`
* Objects are compared by values, not memory

---

# 📁 05_dataclass_immutable.py

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Config:
    api_key: str
    timeout: int

c = Config("ABC123", 30)

print(c.api_key)
```

### 💡 Explanation:

* `frozen=True` makes object **immutable**
* You cannot change values after creation
* Useful for configs, constants

---

# 📁 06_dataclass_repr_eq.py

```python
from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    salary: int

e1 = Employee("A", 50000)
e2 = Employee("A", 50000)

print(e1)
print(e1 == e2)
```

### 💡 Explanation:

* `__repr__` → readable object output
* `__eq__` → compares values automatically

---

# 📁 07_dataclass_real_world.py

```python
from dataclasses import dataclass

@dataclass
class Order:
    item: str
    price: int
    quantity: int = 1

    def total(self):
        return self.price * self.quantity

o = Order("Laptop", 50000, 2)

print(o)
print(o.total())
```

### 💡 Explanation:

* Dataclasses are perfect for real-world models
* You can still add custom methods

---

# 📁 08_dataclass_sorting.py

```python
from dataclasses import dataclass

@dataclass(order=True)
class Student:
    marks: int
    name: str

students = [
    Student(80, "A"),
    Student(90, "B"),
    Student(70, "C")
]

students.sort()

for s in students:
    print(s)
```

### 💡 Explanation:

* `order=True` enables sorting
* Sorting happens automatically based on fields

---

# 📁 09_practice_student_system.py

```python
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    marks: int

    def passed(self):
        return self.marks >= 40

s1 = Student("Monjur", 85)
s2 = Student("Rahim", 30)

print(s1.passed())
print(s2.passed())
```

### 💡 Explanation:

* Simple real-world system example
* Clean structure using dataclass
* Easy logic inside class

---

# 🎯 Day 15 Summary

Today you learned:

* 🧾 What is a dataclass
* ⚙️ Auto-generated `__init__`, `__repr__`, `__eq__`
* 🔒 Immutable objects using `frozen=True`
* 📊 Sorting objects using `order=True`
* 🧠 Real-world data modeling

---

# Author

**Engr. Md Monjur Bakth Mazumder**

🎓 Diploma in Computer Science and Technology — [Moulvibazar Polytechnic Institute](https://mpi.moulvibazar.gov.bd/)  
🎓 BSc in Computer Science & Engineering (CSE) (Ongoing) — [Sylhet International University](https://siu.edu.bd/)

📧 Email: monjurmbm404@gmail.com

### ⭐ If you find this helpful, don’t forget to **star** the repository!