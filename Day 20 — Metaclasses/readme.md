# 🐍 Python OOP – Day 20 — Metaclasses

---

## 📌 Overview

💡 What is a Metaclass?

A **metaclass** is the “class of a class”.

In simple words:

- A class creates objects
- A metaclass creates classes

So the hierarchy becomes:

- Object → created by Class
- Class → created by Metaclass (`type`)

👉 Everything in Python is an object, even classes themselves.

---

## 🔑 Key Concepts

- `type()` → default metaclass in Python
- Metaclass → controls class creation
- Used for:
  - Dynamic class creation
  - Automatic modifications
  - Validation rules
  - Framework-level design (like Django internals)

---

## 📁 File-by-File Explanation

---

## 📁 01_what_is_metaclass.py

💡 Understanding what a metaclass is

### 📌 Code Example

```python id="m1a1xx"
class Student:
    pass

print(type(Student))
```

### 🧠 Explanation

- A class itself is an object
- `type(Student)` shows who created the class
- Default creator is `type`

---

## 📁 02_type_function_basics.py

💡 Creating classes dynamically using `type()`

### 📌 Code Example

```python id="m2b2yy"
DynamicClass = type(
    "DynamicClass",
    (),
    {
        "greet": lambda self: "Hello from dynamic class"
    }
)

obj = DynamicClass()

print(obj.greet())
```

### 🧠 Explanation

- `type()` can create classes at runtime
- Structure:
  - Class name
  - Base classes
  - Attributes/methods

- Used in frameworks and libraries

---

## 📁 03_metaclass_explained.py

💡 Default metaclass concept

### 📌 Code Example

```python id="m3c3zz"
class MyClass:
    pass

print(type(MyClass))
print(type(type))
```

### 🧠 Explanation

- Every class is created by `type`
- Even `type` itself is a class
- This is the foundation of Python OOP internals

---

## 📁 04_custom_metaclass_basic.py

💡 Creating your own metaclass

### 📌 Code Example

```python id="m4d4aa"
class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class: {name}")
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=MyMeta):
    def hello(self):
        return "Hello World"
```

### 🧠 Explanation

- `__new__` runs when class is created
- Metaclass intercepts class creation process
- Useful for controlling class behavior

---

## 📁 05_metaclass_modifying_class.py

💡 Injecting methods automatically

### 📌 Code Example

```python id="m5e5bb"
class AutoAddMethod(type):
    def __new__(cls, name, bases, dct):
        dct["auto_method"] = lambda self: "Injected Method"
        return super().__new__(cls, name, bases, dct)

class Test(metaclass=AutoAddMethod):
    pass
```

### 🧠 Explanation

- Metaclass modifies class before creation
- Automatically adds methods
- Useful in large frameworks

---

## 📁 06_metaclass_validation.py

💡 Enforcing rules at class creation time

### 📌 Code Example

```python id="m6f6cc"
class NoEmptyClassMeta(type):
    def __new__(cls, name, bases, dct):
        if len(dct) == 0:
            raise Exception("Class cannot be empty!")
        return super().__new__(cls, name, bases, dct)

class ValidClass(metaclass=NoEmptyClassMeta):
    x = 10
```

### 🧠 Explanation

- Metaclass validates class before it exists
- Prevents bad design early
- Used in strict frameworks

---

## 📁 07_real_world_metaclass.py

💡 Real-world usage (registry system)

### 📌 Code Example

```python id="m7g7dd"
class RegistryMeta(type):
    registry = {}

    def __new__(cls, name, bases, dct):
        new_class = super().__new__(cls, name, bases, dct)
        cls.registry[name] = new_class
        return new_class

class A(metaclass=RegistryMeta):
    pass

class B(metaclass=RegistryMeta):
    pass

print(RegistryMeta.registry)
```

### 🧠 Explanation

- Automatically tracks all created classes
- Used in plugins, frameworks, ORMs
- Example: Django model registry system

---

## 📁 08_simple_understanding.py

💡 Mental model of metaclasses

### 📌 Code Example

```python id="m8h8ee"
class MyMeta(type):
    pass

class MyClass(metaclass=MyMeta):
    pass

print(type(MyClass))
print(type(MyMeta))
```

### 🧠 Explanation

- Class → created by metaclass
- Metaclass → created by `type`
- Everything connects to `type`

---

## 📁 09_practice_dynamic_class.py

💡 Dynamic class creation practice

### 📌 Code Example

```python id="m9i9ff"
def say_hi(self):
    return "Hi from dynamic class"

Dynamic = type(
    "Dynamic",
    (),
    {"say_hi": say_hi}
)

obj = Dynamic()

print(obj.say_hi())
```

### 🧠 Explanation

- You create full classes without `class` keyword
- Useful in dynamic frameworks

---

## 🎯 Day 20 Summary

- Learned what metaclasses are
- Understood that classes are objects too
- Explored `type()` as a class factory
- Built custom metaclasses
- Modified classes automatically
- Added validation rules using metaclasses
- Learned real-world registry systems
- Practiced dynamic class creation

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

