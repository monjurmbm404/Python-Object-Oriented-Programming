# 🐍 Python OOP – Day 02: Constructor & Instance Methods

---

## 📌 Overview

In **Day 02**, you move from basic classes to **real-world object creation** 🚀

You will learn how to:

✔ Initialize objects with data  
✔ Use the `__init__` constructor  
✔ Understand the `self` keyword  
✔ Create methods that work with object data

---

## 💡 Why this is important?

Without this concept, classes are just empty structures.

👉 With constructors + methods, your objects become **useful and dynamic**.

---

# ⚙ 01. Constructor (`__init__`)

## 📁 01_constructor_init.py

### 📘 Explanation:

A **constructor** is a special method that runs automatically when you create an object.

### 🧠 Example:

```python
class Student:
    def __init__(self):
        print("Constructor called!")

s1 = Student()
```

✔ No need to call manually  
✔ Runs automatically

---

# ⚙ 02. Constructor with Values

## 📁 02_constructor_with_values.py

### 📘 Explanation:

You can pass values while creating an object.

### 🧠 Example:

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Monjur", 22)
```

✔ `self.name` → stores data in object  
✔ Each object has different values

---

# 🧠 03. `self` Keyword (VERY IMPORTANT)

## 📁 03_self_keyword.py

### 📘 Explanation:

`self` refers to the **current object**

👉 It allows access to:

- Instance variables
- Instance methods

### 🧠 Example:

```python
class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def show(self):
        print(self.brand, self.speed)
```

✔ `self.brand` → belongs to that specific object

---

# 🔧 04. Instance Methods

## 📁 04_instance_methods.py

### 📘 Explanation:

Instance methods are functions inside a class that use object data.

### 🧠 Example:

```python
class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b
```

✔ Works with object values  
✔ Always uses `self`

---

# 👥 05. Multiple Objects

## 📁 05_multiple_objects.py

### 📘 Explanation:

You can create many objects from one class.

### 🧠 Example:

```python
s1 = Student("Monjur", 90)
s2 = Student("Karim", 85)
```

✔ Same class  
✔ Different data

---

# 🧪 Practice Section

---

## 📁 06_practice_product.py

### 📘 What you do:

✔ Create Product objects  
✔ Store name & price  
✔ Display details

---

## 📁 07_practice_user.py

### 📘 What you do:

✔ Create User objects  
✔ Store username & email  
✔ Display information

---

# 🎯 Day 02 Summary

You Learned:

## ⚙ Constructor

✔ `__init__` runs automatically  
✔ Initializes object data

## 🧠 self Keyword

✔ Refers to current object  
✔ Access variables & methods

## 🔧 Instance Methods

✔ Work with object data  
✔ Always use `self`

## 👥 Objects

✔ Multiple objects from same class  
✔ Each object has different data

---

# Author

**Engr. Md Monjur Bakth Mazumder**

🎓 Diploma in Computer Science and Technology — [Moulvibazar Polytechnic Institute](https://mpi.moulvibazar.gov.bd/)  
🎓 BSc in Computer Science & Engineering (CSE) (Ongoing) — [Sylhet International University](https://siu.edu.bd/)

📧 Email: monjurmbm404@gmail.com

### ⭐ If you find this helpful, don’t forget to **star** the repository!
