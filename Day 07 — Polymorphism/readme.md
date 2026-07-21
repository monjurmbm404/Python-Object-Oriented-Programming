# 🐍 Python OOP – Day 07: Polymorphism

---

## 📌 Overview

Welcome to **Day 07 of Python OOP** 🚀

Today you will learn **Polymorphism**, one of the most powerful concepts in OOP.

You will understand how:

✔ The same method can behave differently  
✔ One interface can have multiple forms  
✔ Objects can work dynamically at runtime

---

## 💡 What is Polymorphism?

**Polymorphism** means:

👉 _“One thing, many forms”_

### 🧠 In simple words:

The same method name can perform **different actions depending on the object**.

---

## 🎯 Why Polymorphism is Important?

✔ Makes code flexible  
✔ Reduces complexity  
✔ Improves reusability  
✔ Helps build scalable systems

---

# 🎭 01. Method Overriding

## 📁 01_method_overriding.py

### 📘 Explanation:

When a child class **redefines a method** from the parent class.

### 🧠 Example:

```python id="poly1"
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")
```

### 🔑 Key Idea:

✔ Same method name (`sound`)  
✔ Different behavior in each class

---

# ⏱ 02. Runtime Polymorphism

## 📁 02_runtime_polymorphism.py

### 📘 Explanation:

Python decides **which method to run at runtime**.

### 🧠 Example:

```python id="poly2"
shapes = [Circle(), Rectangle(), Shape()]

for shape in shapes:
    shape.area()
```

### 🔑 Key Idea:

✔ Decision happens while program runs  
✔ Not fixed at compile time

---

# 🦆 03. Duck Typing

## 📁 03_duck_typing.py

### 📘 Explanation:

👉 “If it behaves like a duck, it is a duck”

Python does NOT care about type — only behavior.

### 🧠 Example:

```python id="duck1"
def start_movement(obj):
    obj.move()
```

✔ If object has `.move()` → it works

---

# ⚙ 04. Polymorphism with Functions

## 📁 04_polymorphism_with_functions.py

### 📘 Explanation:

A single function can work with **different types of objects**.

### 🧠 Example:

```python id="funcpoly"
def device_typing(device):
    device.type()
```

✔ Same function  
✔ Different object behavior

---

# 🔁 05. Polymorphism with Inheritance

## 📁 05_polymorphism_with_inheritance.py

### 📘 Explanation:

Child classes modify parent behavior.

### 🧠 Example:

```python id="paypoly"
class Payment:
    def pay(self):
        print("Processing payment")

class CreditCard(Payment):
    def pay(self):
        print("Pay via Credit Card")

class PayPal(Payment):
    def pay(self):
        print("Pay via PayPal")
```

✔ Same method → different payment methods

---

# 🧪 Practice Section

---

## 📁 06_practice_shape.py

### 📘 What you learn:

✔ Different shapes calculate area differently

### 🧠 Example:

```python id="shape1"
Circle(5).area()
Square(4).area()
```

✔ Same method → different formulas

---

## 📁 07_practice_animal.py

### 📘 What you learn:

✔ Animal sounds vary by type

### 🧠 Example:

```python id="animalpoly"
Dog().sound()
Cat().sound()
Cow().sound()
```

✔ Same method → different outputs

---

## 📁 08_practice_payment_system.py

### 📘 What you learn:

✔ Payment system with multiple methods

### 🧠 Example:

```python id="pay2"
Card().pay()
UPI().pay()
Cash().pay()
```

✔ One system → many payment types

---

# 🎯 Day 07 Summary

You Learned:

## 🎭 Polymorphism Basics

✔ One method → multiple behaviors  
✔ Method overriding

## ⏱ Runtime Behavior

✔ Method decided during execution

## 🦆 Duck Typing

✔ Focus on behavior, not type

## ⚙ Flexible Functions

✔ Same function works with different objects

## 🌍 Real-world Usage

✔ Payment systems  
✔ Shape systems  
✔ Animal behavior systems

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

