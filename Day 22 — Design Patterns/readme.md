# 🐍 Python OOP – Day 22 — Design Patterns (Basic Intro)

---

## 📌 Overview

In this day, you learn **design patterns**, which are **proven solutions to common programming problems**.
These patterns help you write **clean, scalable, and reusable code** like professional developers.

---

## 💡 What is a Design Pattern?

A design pattern is a **ready-made solution template** for solving common software design problems.

- 🧠 Think of it as a “best practice”
- 🏗 Helps structure code properly
- 🔄 Makes systems flexible and maintainable

---

## 📁 01_singleton_basic.py

### 💡 Singleton Pattern (Basic)

- 🔒 Only one object is created
- 📦 Shared instance across the program

```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating new instance")
            cls._instance = super().__new__(cls)
        return cls._instance

s1 = Singleton()
s2 = Singleton()

print(s1 is s2)  # True
```

---

## 📁 02_singleton_real_world.py

### 💡 Singleton (Real-world Example)

- 🗄 Used for database connection
- 🔗 Ensures single shared connection

```python
class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Connecting to database...")
            cls._instance = super().__new__(cls)
        return cls._instance

db1 = Database()
db2 = Database()

print(db1 is db2)
```

---

## 📁 03_factory_basic.py

### 💡 Factory Pattern (Basic)

- 🏭 Creates objects without exposing logic
- 🎯 User doesn’t need to know class details

```python
class Dog:
    def speak(self):
        return "Bark"

class Cat:
    def speak(self):
        return "Meow"

class AnimalFactory:
    @staticmethod
    def get_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()

animal = AnimalFactory.get_animal("dog")
print(animal.speak())
```

---

## 📁 04_factory_improved.py

### 💡 Factory (Improved Version)

- ➕ Easily extendable
- 🔓 Follows Open/Closed Principle

```python
class Dog:
    def speak(self):
        return "Bark"

class Cat:
    def speak(self):
        return "Meow"

class Bird:
    def speak(self):
        return "Chirp"

class AnimalFactory:
    _creators = {
        "dog": lambda: Dog(),
        "cat": lambda: Cat(),
        "bird": lambda: Bird()
    }

    @classmethod
    def get_animal(cls, animal_type):
        creator = cls._creators.get(animal_type)
        if creator:
            return creator()
        raise ValueError("Unknown animal")

a = AnimalFactory.get_animal("bird")
print(a.speak())
```

---

## 📁 05_strategy_basic.py

### 💡 Strategy Pattern (Basic)

- 🔄 Change behavior at runtime
- 🎯 Same interface, different logic

```python
class PaymentStrategy:
    def pay(self, amount):
        pass

class CardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} via Card")

class CashPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} via Cash")

class PaymentProcessor:
    def __init__(self, strategy):
        self.strategy = strategy

    def process(self, amount):
        self.strategy.pay(amount)

processor = PaymentProcessor(CardPayment())
processor.process(1000)

processor.strategy = CashPayment()
processor.process(500)
```

---

## 📁 06_strategy_real_world.py

### 💡 Strategy (Real-world Example)

- 🔃 Change algorithms dynamically
- 📊 Example: sorting data

```python
class SortStrategy:
    def sort(self, data):
        pass

class AscendingSort(SortStrategy):
    def sort(self, data):
        return sorted(data)

class DescendingSort(SortStrategy):
    def sort(self, data):
        return sorted(data, reverse=True)

class DataProcessor:
    def __init__(self, strategy):
        self.strategy = strategy

    def process(self, data):
        return self.strategy.sort(data)

data = [5, 2, 9, 1]

processor = DataProcessor(AscendingSort())
print(processor.process(data))

processor.strategy = DescendingSort()
print(processor.process(data))
```

---

## 📁 07_combined_example.py

### 💡 Factory + Strategy Combined

- 🔗 Combine multiple patterns
- 🧠 Build flexible systems

```python
class Card:
    def pay(self, amount):
        print("Card:", amount)

class Cash:
    def pay(self, amount):
        print("Cash:", amount)

class PaymentFactory:
    @staticmethod
    def get_method(method):
        if method == "card":
            return Card()
        return Cash()

class PaymentProcessor:
    def __init__(self, method):
        self.strategy = PaymentFactory.get_method(method)

    def process(self, amount):
        self.strategy.pay(amount)

p = PaymentProcessor("card")
p.process(1000)
```

---

## 📁 08_practice_singleton_logger.py

### 💡 Practice: Logger Singleton

- 📝 Single logger instance
- 🔁 Shared across app

```python
class Logger:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def log(self, msg):
        print("LOG:", msg)

l1 = Logger()
l2 = Logger()

l1.log("Hello")

print(l1 is l2)
```

---

## 📁 09_practice_strategy_discount.py

### 💡 Practice: Discount Strategy

- 💰 Dynamic discount logic
- 🔄 Change calculation anytime

```python
class DiscountStrategy:
    def apply(self, price):
        pass

class TenPercent(DiscountStrategy):
    def apply(self, price):
        return price * 0.9

class FixedDiscount(DiscountStrategy):
    def apply(self, price):
        return price - 100

class Cart:
    def __init__(self, strategy):
        self.strategy = strategy

    def checkout(self, price):
        return self.strategy.apply(price)

cart = Cart(TenPercent())
print(cart.checkout(1000))

cart.strategy = FixedDiscount()
print(cart.checkout(1000))
```

---

## 🎯 Day 22 Summary

- 🔒 Singleton → one instance only
- 🏭 Factory → object creation control
- 🔄 Strategy → change behavior dynamically
- 🧠 Build flexible and scalable systems
- 🔗 Combine patterns for real-world design

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

