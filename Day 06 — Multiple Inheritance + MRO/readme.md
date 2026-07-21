# 🐍 Python OOP – Day 06: Multiple Inheritance + MRO

---

## 📌 Overview

Welcome to **Day 06 of Python OOP** 🚀

Today you will learn one of the most powerful (and slightly tricky) concepts:

👉 **Multiple Inheritance**
👉 **Method Resolution Order (MRO)**

You will understand how a class can inherit from **multiple parent classes** and how Python decides **which method to run first**.

---

## 💡 What is Multiple Inheritance?

**Multiple Inheritance** means:

👉 A class can inherit from **more than one parent class**

### 🧠 Simple Idea:

A child class can get features from **multiple parents at the same time**.

---

## 🎯 Why it is Important?

✔ Reuse code from multiple classes  
✔ Build flexible systems  
✔ Combine different functionalities  
✔ Used in real-world frameworks

---

# 🧬 01. Multiple Inheritance Basics

## 📁 01_multiple_inheritance_basics.py

### 📘 Explanation:

A child class can access methods from both parents.

### 🧠 Example:

```python id="9h3x1a"
class Father:
    def skills(self):
        print("Father: Gardening, Driving")

class Mother:
    def skills(self):
        print("Mother: Cooking, Painting")

class Child(Father, Mother):
    def my_skills(self):
        print("Child: Sports, Coding")

c = Child()

c.my_skills()
c.skills()
```

### ⚠ Important:

👉 Both parents have `skills()`  
👉 Which one will run? → MRO decides

---

# 💎 02. Diamond Problem

## 📁 02_diamond_problem.py

### 📘 Explanation:

This problem happens when:

👉 Multiple parents inherit from a common ancestor  
👉 Same method exists in multiple paths

### 🧠 Example:

```python id="d2m1p0"
class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(A):
    def show(self):
        print("Class C")

class D(B, C):
    pass

d = D()
d.show()
```

### ⚠ Problem:

Python must decide:

👉 B or C → which one first?

---

# 🧭 03. Method Resolution Order (MRO)

## 📁 03_mro_method.py

### 📘 Explanation:

**MRO = Order Python uses to find methods**

👉 Left to right priority  
👉 Uses C3 linearization

### 🧠 Example:

```python id="mro123"
print(D.mro())
print(D.__mro__)
```

✔ Shows search order of classes  
✔ First match is used

---

# 🔁 04. Left-to-Right Priority

## 📁 04_mro_with_multiple_methods.py

### 📘 Explanation:

Python checks parent classes **from left to right**

### 🧠 Example:

```python id="lrmro1"
class D(B, C, A):
    pass

obj = D()
obj.display()
```

✔ B runs first  
✔ Then C  
✔ Then A

---

# ⚙ 05. super() in Multiple Inheritance

## 📁 05_super_with_multiple_inheritance.py

### 📘 Explanation:

`super()` follows **MRO automatically**

### 🧠 Example:

```python id="supermro"
class D(B, C):
    def show(self):
        print("D")
        super().show()
```

✔ No need to manually call parent  
✔ Python handles chain automatically

---

# 🌍 06. Real-World Example

## 📁 06_real_world_multiple_inheritance.py

### 📘 Explanation:

Multiple inheritance is used when combining features:

👉 Camera + Phone → Smartphone

### 🧠 Example:

```python id="smart1"
class Camera:
    def camera_feature(self):
        print("Taking photo")

class Phone:
    def call_feature(self):
        print("Making call")

class SmartPhone(Camera, Phone):
    def app_feature(self):
        print("Running apps")
```

✔ One device = multiple features

---

# 🧠 07. MRO Flow Understanding

## 📁 07_mro_explanation_flow.py

### 📘 Explanation:

Python always follows:

👉 Left → Right → Parent → Grandparent

### 🧠 Example:

```python id="flowmro"
print(D.mro())
d.process()
```

✔ First matching method is executed

---

# 🧪 Practice Section

---

## 📁 08_practice_university_system.py

### 📘 What you learn:

✔ Combine multiple roles in one class  
✔ Teacher + Researcher + Person

### 🧠 Example:

```python id="uni1"
class Professor(Teacher, Researcher, Person):
    pass
```

✔ One class → multiple responsibilities

---

## 📁 09_practice_employee_system.py

### 📘 What you learn:

✔ Worker + Developer + Designer

### 🧠 Example:

```python id="emp1"
class Freelancer(Worker, Developer, Designer):
    pass
```

✔ Real-world multi-skill system

---

# 🎯 Day 06 Summary

You Learned:

## 🧬 Multiple Inheritance

✔ One class → multiple parents  
✔ Combine features

## 💎 Diamond Problem

✔ Same method from multiple paths  
✔ Can cause confusion

## 🧭 MRO (Method Resolution Order)

✔ Python decides execution order  
✔ Left to right priority  
✔ Use `mro()` to check order

## ⚙ super() Behavior

✔ Follows MRO automatically  
✔ Used in complex inheritance

## 🧪 Practice

✔ University system  
✔ Employee system

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

