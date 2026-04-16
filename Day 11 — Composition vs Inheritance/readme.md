# 🐍 Python OOP – Day 11: Composition vs Inheritance

---

## 📌 Overview

Welcome to **Day 11 of Python OOP** 🚀

Today you will learn an **important design concept**:

👉 **Composition vs Inheritance**

This is where you start thinking like a **real software engineer** 🧠

You will understand how to:

- Design better class relationships
- Choose between inheritance and composition
- Build flexible and scalable systems
- Reduce code complexity

---

## 💡 What is Inheritance vs Composition?

### 🧬 Inheritance (is-a)

👉 A child class **inherits** from a parent class

- Example: Dog **is-a** Animal
- Used when classes share the same nature

---

### 🧩 Composition (has-a)

👉 A class **contains another class as a part**

- Example: Car **has-a** Engine
- Used to build complex systems

---

## 🎯 Why This is Important?

- Helps you design clean architecture
- Avoids poor class relationships
- Improves code flexibility
- Makes systems easier to maintain

---

# 🔍 01. is-a vs has-a

## 📁 01_is_a_vs_has_a.py

### 📘 Explanation:

Two types of relationships:

- **is-a → Inheritance**
- **has-a → Composition**

### 🧠 Example:

```python id="rel1"
class Dog(Animal):  # is-a
    pass

class Car:
    def __init__(self):
        self.engine = Engine()  # has-a
```

### 🔑 Key Idea:

- Use inheritance for **same-type relationships**
- Use composition for **part-of relationships**

---

# 🧩 02. Composition Basics

## 📁 02_composition_basics.py

### 📘 Explanation:

Composition builds complex objects using smaller ones.

### 🧠 Example:

```python id="comp1"
class Computer:
    def __init__(self):
        self.cpu = CPU()
```

- Computer uses CPU
- CPU works independently

---

# ⚖ 03. Composition vs Inheritance

## 📁 03_composition_vs_inheritance.py

### 📘 Explanation:

| Concept     | Type              |
| ----------- | ----------------- |
| Inheritance | Tight coupling    |
| Composition | Loose coupling ⭐ |

### 🧠 Problem Example:

```python id="prob1"
class Bird:
    def fly(self):
        print("Flying")
```

❌ Not all birds can fly → poor design

### ✅ Better Solution:

```python id="comp2"
class Bird:
    def __init__(self, fly_ability=None):
        self.fly_ability = fly_ability
```

- Flexible behavior
- No incorrect assumptions

---

# 🔁 04. Code Reuse Strategies

## 📁 04_code_reuse_strategies.py

### 📘 Explanation:

Two main reuse strategies:

### 🧬 Inheritance:

```python id="reuse1"
class AdvancedCalculator(Calculator):
    pass
```

### 🧩 Composition:

```python id="reuse2"
class App:
    def __init__(self):
        self.adder = Adder()
```

### 🔑 Key Idea:

- Inheritance → extend existing class
- Composition → combine smaller objects

---

# 🌍 05. Real-World Composition

## 📁 05_real_world_composition.py

### 📘 Explanation:

Real systems are built using composition.

### 🧠 Example:

```python id="real1"
class Car:
    def __init__(self):
        self.engine = Engine()
        self.battery = Battery()
```

- Car = Engine + Battery
- Components work independently

---

# 💉 06. Dependency Injection (Advanced)

## 📁 06_dependency_injection_style.py

### 📘 Explanation:

Dependency is passed from outside the class.

👉 This is called **Dependency Injection**

### 🧠 Example:

```python id="di1"
app = App(Database())
```

### 🔑 Key Idea:

- Improves flexibility
- Makes testing easier
- Reduces tight coupling

---

# 🧪 Practice Section

---

## 📁 07_practice_order_system.py

### 📘 What you learn:

- Order contains multiple products
- Calculate total dynamically

### 🧠 Example:

```python id="order1"
o.add_product(Product("Laptop", 50000))
```

- Order HAS products
- Uses composition

---

## 📁 08_practice_user_profile.py

### 📘 What you learn:

- User has address
- Clean object relationship

### 🧠 Example:

```python id="user1"
user = User("Monjur", Address("Sylhet", "Bangladesh"))
```

- User HAS address
- Real-world modeling

---

# 🎯 Day 11 Summary

You Learned:

## 🧬 Inheritance

- is-a relationship
- Reuse through extension

## 🧩 Composition

- has-a relationship
- Build systems using parts

## ⚖ Key Difference

- Inheritance → tight coupling
- Composition → loose coupling (recommended)

## 💉 Advanced Concept

- Dependency Injection
- Flexible system design

## 🌍 Real-world Thinking

- Better architecture decisions
- Scalable and maintainable code

---

# Author

**Engr. Md Monjur Bakth Mazumder**

🎓 Diploma in Computer Science and Technology — [Moulvibazar Polytechnic Institute](https://mpi.moulvibazar.gov.bd/)  
🎓 BSc in Computer Science & Engineering (CSE) (Ongoing) — [Sylhet International University](https://siu.edu.bd/)

📧 Email: monjurmbm404@gmail.com

### ⭐ If you find this helpful, don’t forget to **star** the repository!
