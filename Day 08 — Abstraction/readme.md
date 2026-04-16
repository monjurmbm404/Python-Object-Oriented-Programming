# 🐍 Python OOP – Day 08: Abstraction

---

## 📌 Overview

Welcome to **Day 08 of Python OOP** 🚀

Today you will learn **Abstraction**, one of the most important principles of Object-Oriented Programming.

You will understand how to:

✔ Hide internal implementation details  
✔ Show only essential features to the user  
✔ Use abstract classes and abstract methods  
✔ Build real-world system designs

---

## 💡 What is Abstraction?

**Abstraction** means:

👉 _Hiding internal details and showing only what is necessary_

### 🧠 In simple words:

You use something without knowing **how it works internally**.

Example:

✔ You drive a car  
✔ But you don’t know how engine works internally

---

## 🎯 Why Abstraction is Important?

✔ Reduces complexity  
✔ Improves code organization  
✔ Hides unnecessary implementation details  
✔ Makes code more secure and clean  
✔ Helps in large system design

---

# 🧠 01. Abstract Class (Basic)

## 📁 01_abstract_class_basic.py

### 📘 Explanation:

An **abstract class**:

👉 Cannot fully represent a real object  
👉 Used as a base structure

### 🧠 Example:

```python id="abs1"
from abc import ABC

class Vehicle(ABC):
    pass
```

✔ Abstract class acts as a blueprint  
✔ Not useful alone without methods

---

# ⚙ 02. Abstract Methods

## 📁 02_abstract_methods.py

### 📘 Explanation:

An **abstract method**:

👉 Declared in parent class  
👉 Must be implemented in child class

### 🧠 Example:

```python id="abs2"
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass
```

### 🔑 Key Idea:

✔ Child class MUST define this method  
✔ Otherwise object cannot be created

---

# 🚫 03. Abstract Class Rules

## 📁 03_abstract_class_rules.py

### 📘 Explanation:

Rules of abstraction:

✔ You cannot create object of abstract class  
✔ Child class must implement all abstract methods

### 🧠 Example:

```python id="abs3"
# Shape() ❌ cannot be created

class Circle(Shape):
    def area(self):
        print("Calculating area")
```

✔ Forces structure consistency

---

# 🔌 04. Interface-like Design

## 📁 04_interface_like_design.py

### 📘 Explanation:

Python does not have real interfaces, but:

👉 Abstract classes act like interfaces

### 🧠 Example:

```python id="abs4"
class PaymentGateway(ABC):
    def pay(self, amount):
        pass
```

✔ Different classes implement same method differently

---

# 🌍 05. Real-World Abstraction

## 📁 05_real_world_abstraction.py

### 📘 Explanation:

User interacts only with functions:

👉 Login  
👉 Transfer money

But internal logic is hidden.

### 🧠 Example:

```python id="abs5"
app.login()
app.transfer_money(5000)
```

✔ User does not see internal processing

---

# 🔁 06. Multiple Implementations

## 📁 06_abstract_with_multiple_classes.py

### 📘 Explanation:

Same abstract class → different behaviors.

### 🧠 Example:

```python id="abs6"
Email().send()
SMS().send()
Push().send()
```

✔ Same function → different output

---

# ⚖ 07. Abstraction vs Encapsulation

## 📁 07_abstraction_vs_encapsulation.py

### 📘 Explanation:

| Concept       | Meaning                             |
| ------------- | ----------------------------------- |
| Abstraction   | Hides implementation (what it does) |
| Encapsulation | Hides data (how it is protected)    |

### 🧠 Example:

```python id="abs7"
def area():
    return 3.14 * r * r
```

✔ You don’t see internal calculation logic

---

# 🧪 Practice Section

---

## 📁 08_practice_vehicle_system.py

### 📘 What you learn:

✔ Abstract vehicle system  
✔ Different start mechanisms

### 🧠 Example:

```python id="abs8"
Car().start()
Bike().start()
```

✔ Same method → different behavior

---

## 📁 09_practice_payment_system.py

### 📘 What you learn:

✔ Payment abstraction system  
✔ Multiple payment methods

### 🧠 Example:

```python id="abs9"
Bank().pay()
Card().pay()
```

✔ Unified interface for payments

---

# 🎯 Day 08 Summary

You Learned:

## 🧠 Abstraction Basics

✔ Hides implementation details  
✔ Shows only essential features

## ⚙ Abstract Classes

✔ Cannot be instantiated
✔ Used as blueprint

## 🔌 Abstract Methods

✔ Must be implemented in child classes

## 🌍 Real-World Usage

✔ Payment systems  
✔ Vehicle systems  
✔ Notification systems

## ⚖ Key Difference

✔ Abstraction → hides complexity  
✔ Encapsulation → hides data

---

# Author

**Engr. Md Monjur Bakth Mazumder**

🎓 Diploma in Computer Science and Technology — [Moulvibazar Polytechnic Institute](https://mpi.moulvibazar.gov.bd/)  
🎓 BSc in Computer Science & Engineering (CSE) (Ongoing) — [Sylhet International University](https://siu.edu.bd/)

📧 Email: monjurmbm404@gmail.com

### ⭐ If you find this helpful, don’t forget to **star** the repository!
