# 🐍 Python OOP – Day 01: Basics + Class & Object

---

## 📌 Overview

Welcome to **Object-Oriented Programming (OOP)** 🚀

In this day, you are starting one of the **most important concepts in Python** that is used in:

✔ Real-world applications  
✔ Backend development  
✔ Large-scale systems

---

## 💡 What is OOP?

**OOP (Object-Oriented Programming)** is a way of writing code using:

✔ **Classes** (blueprints)  
✔ **Objects** (real instances)

👉 Instead of writing everything in one place, OOP helps you **organize your code like real-world objects**.

---

## 🎯 Why OOP is Important?

✔ Makes code reusable  
✔ Easy to manage large projects  
✔ Cleaner and structured code  
✔ Matches real-world thinking

---

# 🏗 01. Class vs Object

## 📁 02_class_vs_object.py

### 📘 Explanation:

Think like this:

- **Class** → Design / Blueprint
- **Object** → Real item created from that design

### 🧠 Example:

```python
class Car:
    pass

car1 = Car()
car2 = Car()
```

✔ `Car` is a class  
✔ `car1`, `car2` are objects

---

# 🏗 02. Creating a Class

## 📁 03_creating_class.py

### 📘 Explanation:

A class is created using the `class` keyword.

### 🧠 Example:

```python
class Student:
    name = "Unknown"
    age = 0

s1 = Student()

print(s1.name)
print(s1.age)
```

✔ Class defines structure  
✔ Object uses that structure

---

# 🧍 03. Creating Objects

## 📁 04_creating_objects.py

### 📘 Explanation:

Each object can have its **own data**.

### 🧠 Example:

```python
s1 = Student()
s2 = Student()

s1.name = "Monjur"
s2.name = "Rahim"
```

✔ Same class  
✔ Different values

---

# 📦 04. Attributes (Very Important)

## 📁 05_attributes_basics.py

### 📘 Explanation:

Attributes = variables inside a class or object

### 🔹 Types:

### 1. Class Attribute

Shared by all objects

```python
class Car:
    wheels = 4
```

### 2. Instance Attribute

Different for each object

```python
c1.brand = "Toyota"
c2.brand = "BMW"
```

---

# 🧪 Practice Section

---

## 📁 06_practice_student.py

### 📘 What you do:

✔ Create student objects  
✔ Assign name & marks

---

## 📁 07_practice_car.py

### 📘 What you do:

✔ Create car objects  
✔ Assign brand & speed

---

# 🎯 Day 01 Summary

You Learned:

## 🧠 OOP Basics

✔ What is OOP  
✔ Why it is important

## 🏗 Class & Object

✔ Class = blueprint  
✔ Object = real instance

## 📦 Attributes

✔ Class attributes  
✔ Instance attributes

## 🧪 Practice

✔ Student example  
✔ Car example

---

# Author

**Engr. Md Monjur Bakth Mazumder**

🎓 Diploma in Computer Science and Technology — [Moulvibazar Polytechnic Institute](https://mpi.moulvibazar.gov.bd/)  
🎓 BSc in Computer Science & Engineering (CSE) (Ongoing) — [Sylhet International University](https://siu.edu.bd/)

📧 Email: monjurmbm404@gmail.com

### ⭐ If you find this helpful, don’t forget to **star** the repository!
