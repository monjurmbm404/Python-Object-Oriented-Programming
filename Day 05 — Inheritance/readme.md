# 🐍 Python OOP – Day 05: Inheritance

---

## 📌 Overview

Welcome to **Day 05 of Python OOP** 🚀

Today you will learn **Inheritance**, one of the most powerful features of Object-Oriented Programming.

You will understand how to:

✔ Reuse code from existing classes  
✔ Create relationships between classes  
✔ Use parent and child classes  
✔ Modify and extend existing behavior

---

## 💡 What is Inheritance?

**Inheritance** means:

👉 A class can **inherit properties and methods** from another class

### 🧠 In simple words:

You can create a new class using an existing class **without rewriting code**.

---

## 🎯 Why Inheritance is Important?

✔ Code reusability (no need to write same code again)
✔ Cleaner and organized structure
✔ Easy to maintain large applications
✔ Helps build real-world relationships

---

# 🧬 01. Single Inheritance

## 📁 01_single_inheritance.py

### 📘 Explanation:

**Single inheritance** means:

👉 One child class inherits from one parent class

### 🧠 Example:

```python
class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

d = Dog()

d.eat()   # from parent
d.bark()  # from child
```

✔ `Dog` inherits from `Animal`  
✔ Can use both parent and child methods

---

# ⚙ 02. Inheritance with Constructor

## 📁 02_single_inheritance_with_constructor.py

### 📘 Explanation:

When using constructors:

✔ Child class can have its own constructor  
✔ Parent constructor can be called using `super()`

### 🧠 Example:

```python
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks

s = Student("Monjur", 90)

print(s.name)
print(s.marks)
```

✔ `super()` calls parent constructor  
✔ Avoids duplicate code

---

# 🔗 03. Multilevel Inheritance

## 📁 03_multilevel_inheritance.py

### 📘 Explanation:

Inheritance can form a chain:

👉 Grandparent → Parent → Child

### 🧠 Example:

```python
class Grandparent:
    def show_grandparent(self):
        print("I am Grandparent")

class Parent(Grandparent):
    def show_parent(self):
        print("I am Parent")

class Child(Parent):
    def show_child(self):
        print("I am Child")

c = Child()

c.show_grandparent()
c.show_parent()
c.show_child()
```

✔ Child gets access to all levels

---

# ⚡ 04. super() Keyword

## 📁 04_super_keyword.py

### 📘 Explanation:

`super()` is used to:

✔ Call parent class methods  
✔ Call parent constructor  
✔ Avoid direct class name usage

### 🧠 Example:

```python
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog barks")

d = Dog()
d.sound()
```

✔ Calls parent + child method together

---

# 🔁 05. Method Reuse

## 📁 05_method_reuse.py

### 📘 Explanation:

Inheritance allows **reusing existing methods**.

### 🧠 Example:

```python
class Calculator:
    def add(self, a, b):
        return a + b

class AdvancedCalculator(Calculator):
    def square(self, x):
        return x * x

calc = AdvancedCalculator()

print(calc.add(10, 5))  # reused
print(calc.square(4))
```

✔ No need to rewrite `add()`

---

# 🔄 06. Method Overriding

## 📁 06_method_overriding.py

### 📘 Explanation:

Child class can **change the behavior** of parent method.

### 🧠 Example:

```python
class Animal:
    def sound(self):
        print("Animal sound")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

a = Animal()
c = Cat()

a.sound()
c.sound()
```

✔ Same method name  
✔ Different output

---

# 🌍 07. Real-World Example

## 📁 07_real_world_example.py

### 📘 Explanation:

Inheritance is used in real systems like:

👉 Employee → Developer

### 🧠 Example:

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def show_details(self):
        print(self.name, self.salary, self.language)

dev = Developer("Monjur", 50000, "Python")
dev.show_details()
```

✔ Developer inherits Employee data

---

# 🧪 Practice Section

---

## 📁 08_practice_vehicle.py

### 📘 What you learn:

✔ Base class → Vehicle  
✔ Child class → Car  
✔ Using `super()`

### 🧠 Example:

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

c = Car("Toyota", "Corolla")
print(c.brand, c.model)
```

---

## 📁 09_practice_bank.py

### 📘 What you learn:

✔ Parent class → Account  
✔ Child class → SavingsAccount  
✔ Adding new functionality

### 🧠 Example:

```python
class Account:
    def __init__(self, balance):
        self.balance = balance

class SavingsAccount(Account):
    def add_interest(self):
        self.balance += 100

acc = SavingsAccount(1000)
acc.add_interest()

print(acc.balance)
```

---

# 🎯 Day 05 Summary

You Learned:

## 🧬 Inheritance Basics

✔ Parent & Child class  
✔ Code reuse

## ⚙ super()

✔ Calls parent constructor/method

## 🔗 Types

✔ Single inheritance  
✔ Multilevel inheritance

## 🔁 Method Concepts

✔ Method reuse  
✔ Method overriding

## 🧪 Practice

✔ Vehicle system  
✔ Bank system

---

# Author

**Engr. Md Monjur Bakth Mazumder**

🎓 Diploma in Computer Science and Technology — [Moulvibazar Polytechnic Institute](https://mpi.moulvibazar.gov.bd/)  
🎓 BSc in Computer Science & Engineering (CSE) (Ongoing) — [Sylhet International University](https://siu.edu.bd/)

📧 Email: monjurmbm404@gmail.com

### ⭐ If you find this helpful, don’t forget to **star** the repository!
