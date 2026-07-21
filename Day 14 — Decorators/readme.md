# 🐍 Python OOP – Day 14: Decorators in OOP

---

## 📌 Overview

In this day, you will learn **Decorators in Python**, especially how they work in OOP 🎯

Decorators help you:

- ⚡ Add extra functionality to functions/methods
- 🧼 Keep code clean and reusable
- 🔄 Avoid repeating the same logic

---

## 💡 What is a Decorator?

A **decorator** is a function that:

- 🔹 Takes another function as input
- 🔹 Adds extra behavior
- 🔹 Returns a new function

👉 You don’t change the original function — you **wrap it**

---

# 🔁 01. Function Decorator (Basic)

## 📁 01_function_decorator_recap.py

### 📘 Explanation:

- Adds behavior **before and after** a function

### 🧠 Example:

```python
def my_decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

### 🧠 Key Points:

- 🔹 `@my_decorator` wraps the function
- 🔹 No change to original function code

---

# 🔢 02. Decorator with Arguments

## 📁 02_decorator_with_arguments.py

### 📘 Explanation:

- Works with functions that have parameters

### 🧠 Example:

```python
def logger(func):
    def wrapper(*args, **kwargs):
        print("Arguments:", args, kwargs)
        result = func(*args, **kwargs)
        print("Function executed")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

print(add(5, 3))
```

### 🧠 Key Points:

- 🔹 Use `*args, **kwargs`
- 🔹 Makes decorator flexible

---

# 🧩 03. Method Decorator (OOP)

## 📁 03_method_decorator.py

### 📘 Explanation:

- Works with class methods
- Must handle `self`

### 🧠 Example:

```python
def log_method(func):
    def wrapper(self, *args, **kwargs):
        print(f"Calling method: {func.__name__}")
        return func(self, *args, **kwargs)
    return wrapper

class Calculator:
    @log_method
    def multiply(self, a, b):
        return a * b

c = Calculator()
print(c.multiply(4, 5))
```

### 🧠 Key Points:

- 🔹 First parameter is `self`
- 🔹 Useful for logging/debugging

---

# 🏷 04. @property (Getter)

## 📁 04_property_getter.py

### 📘 Explanation:

- Turns method into attribute
- No need to use `()`

### 🧠 Example:

```python
class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

p = Product(500)

print(p.price)
```

### 🧠 Key Points:

- 🔹 Clean syntax
- 🔹 Used for controlled access

---

# ⚙️ 05. @property Setter

## 📁 05_property_setter.py

### 📘 Explanation:

- Controls how value is set
- Adds validation

### 🧠 Example:

```python
class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            print("Invalid price")
        else:
            self._price = value

p = Product(500)

p.price = 1000
print(p.price)

p.price = -200
```

### 🧠 Key Points:

- 🔹 Prevent invalid data
- 🔹 Adds safety

---

# 🗑 06. @property Deleter

## 📁 06_property_deleter.py

### 📘 Explanation:

- Controls deletion of attribute

### 🧠 Example:

```python
class User:
    def __init__(self, username):
        self._username = username

    @property
    def username(self):
        return self._username

    @username.deleter
    def username(self):
        print("Deleting username...")
        del self._username

u = User("monjur_dev")

print(u.username)

del u.username
```

### 🧠 Key Points:

- 🔹 Custom delete behavior
- 🔹 Useful in secure systems

---

# 🔄 07. Combined Property

## 📁 07_combined_property.py

### 📘 Explanation:

- Combines getter + setter + deleter

### 🧠 Example:

```python
class Account:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            print("Invalid balance")
        else:
            self._balance = value

    @balance.deleter
    def balance(self):
        print("Balance deleted")
        del self._balance

acc = Account(1000)

print(acc.balance)

acc.balance = 1500
print(acc.balance)

del acc.balance
```

---

# 🧪 Practice Section

---

## 📁 08_practice_logger_decorator.py

### 📘 Task:

- 🔹 Create decorator
- 🔹 Log method execution

---

## 📁 09_practice_bank_property.py

### 📘 Task:

- 🔹 Use property for balance
- 🔹 Add validation logic

---

# 🎯 Day 14 Summary

## 🎯 Decorators

- 🔹 Wrap functions
- 🔹 Add extra behavior
- 🔹 Keep code clean

## 🧩 Method Decorators

- 🔹 Work with class methods
- 🔹 Use `self`

## 🏷 Property

- 🔹 Getter → read value
- 🔹 Setter → control update
- 🔹 Deleter → control delete

## 🧠 Design Understanding

- 🔹 Cleaner code structure
- 🔹 Better data control
- 🔹 Real-world application ready

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

