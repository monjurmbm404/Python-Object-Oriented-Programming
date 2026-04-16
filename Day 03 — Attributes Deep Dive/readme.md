# 🐍 Python OOP – Day 03: Attributes Deep Dive

---

## 📌 Overview

In **Day 03**, you will go deeper into **class behavior and attributes**.

You will learn how Python objects store data in different ways and how to control how objects are displayed.

---

## 💡 Why this is important?

✔ Helps you understand real object behavior  
✔ Used in real projects (APIs, apps, systems)  
✔ Very important for interviews

---

# 🧠 01. Instance vs Class Variables

## 📁 01_instance_vs_class_variables.py

### 📘 Explanation:

There are **two types of variables in OOP**:

---

### 🔹 Class Variable

✔ Shared by all objects  
✔ Same value for every instance

```python id="v9t3xg"
class Student:
    school = "ABC School"
```

---

### 🔹 Instance Variable

✔ Unique for each object  
✔ Defined inside constructor

```python id="p3kq2m"
self.name = name
```

---

### ⚠ Important Concept:

```python id="k8q2ll"
Student.school = "XYZ School"
```

✔ Changes for ALL objects

---

# 🧾 02. Default Values

## 📁 02_default_values.py

### 📘 Explanation:

You can give **default values** in constructor.

### 🧠 Example:

```python id="n7f2aa"
def __init__(self, name="Unknown", price=0):
```

✔ If no value → default is used

---

# ⚡ 03. Dynamic Attributes

## 📁 03_dynamic_attributes.py

### 📘 Explanation:

Python allows adding attributes **after object creation**

### 🧠 Example:

```python id="d8x1aa"
u1.age = 22
u1.email = "test@email.com"
```

✔ Very flexible feature of Python

---

# 🧾 04. `__str__()` Method

## 📁 04_str_method.py

### 📘 Explanation:

Used to define **user-friendly output** when printing an object.

### 🧠 Example:

```python id="s1k2lm"
def __str__(self):
    return f"Student: {self.name}"
```

✔ Makes objects readable when printed

---

# 🔍 05. `__repr__()` Method

## 📁 05_repr_method.py

### 📘 Explanation:

Used for **debugging purposes**

### 🧠 Example:

```python id="r2k9pp"
def __repr__(self):
    return f"Product(name={self.name})"
```

✔ Used by developers  
✔ More technical output

---

# ⚖ 06. **str** vs **repr**

## 📁 06_str_vs_repr.py

### 📘 Difference:

| Method     | Purpose        |
| ---------- | -------------- |
| `__str__`  | User-friendly  |
| `__repr__` | Debug-friendly |

---

# 🧪 Practice Section

---

## 📁 07_practice_student.py

### 📘 What you learn:

✔ Class variables  
✔ Default values  
✔ String formatting

---

## 📁 08_practice_product.py

### 📘 What you learn:

✔ Product modeling  
✔ Debug representation

---

# 🎯 Day 03 Summary

You Learned:

## 🧠 Variables

✔ Class variable (shared)  
✔ Instance variable (unique)  
✔ Default values

---

## ⚡ Dynamic Features

✔ Add attributes at runtime

---

## 🧾 Object Representation

✔ `__str__()` → user-friendly  
✔ `__repr__()` → debug-friendly

---

# Author

**Engr. Md Monjur Bakth Mazumder**

🎓 Diploma in Computer Science and Technology — [Moulvibazar Polytechnic Institute](https://mpi.moulvibazar.gov.bd/)  
🎓 BSc in Computer Science & Engineering (CSE) (Ongoing) — [Sylhet International University](https://siu.edu.bd/)

📧 Email: monjurmbm404@gmail.com

### ⭐ If you find this helpful, don’t forget to **star** the repository!
