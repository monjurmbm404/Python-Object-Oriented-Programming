# 🐍 Python OOP – Day 04: Encapsulation

---

## 📌 Overview

Welcome to **Day 04 of Python OOP** 🚀

Today you will learn **Encapsulation**, one of the **core pillars of Object-Oriented Programming**.

You will understand how to:

✔ Protect data inside a class  
✔ Control access to variables  
✔ Use private and protected variables  
✔ Apply getter & setter methods  
✔ Write cleaner code using `@property`

---

## 💡 What is Encapsulation?

**Encapsulation** means:

👉 **Wrapping data (variables) and methods together inside a class**
👉 **Restricting direct access to some data**

### 🧠 In simple words:

You **hide sensitive data** and allow access **only in a controlled way**.

---

## 🎯 Why Encapsulation is Important?

✔ Protects data from unwanted changes  
✔ Improves security  
✔ Makes code more controlled and maintainable  
✔ Helps in validation (checking correct values)

---

# 🔐 01. Encapsulation Basics

## 📁 01_encapsulation_basics.py

### 📘 Explanation:

In Python, variables can have different access levels:

```python
self.name      # Public
self._age      # Protected (convention)
self.__marks   # Private
```

### 🧠 Key Idea:

✔ Public → accessible anywhere  
✔ Protected → should be used internally  
✔ Private → hidden from outside

---

# 🔐 02. Public vs Protected vs Private

## 📁 02_public_protected_private.py

### 📘 Explanation:

Python does not strictly enforce access control, but follows **naming conventions**:

| Type      | Syntax  | Access Level            |
| --------- | ------- | ----------------------- |
| Public    | `var`   | Anywhere                |
| Protected | `_var`  | Inside class / subclass |
| Private   | `__var` | Restricted              |

### 🧠 Important:

✔ You _can_ access protected variables  
✔ Private variables are **not directly accessible**

---

# 🧠 03. Name Mangling

## 📁 03_name_mangling.py

### 📘 Explanation:

Python changes private variable names internally:

```
__var  →  _ClassName__var
```

### 🧠 Example:

```python
obj._Test__secret
```

✔ This is called **Name Mangling**  
✔ Used to avoid accidental access

---

# ⚙ 04. Getter & Setter

## 📁 04_getter_setter.py

### 📘 Explanation:

Instead of accessing private data directly, we use:

✔ **Getter** → to read value  
✔ **Setter** → to update value safely

### 🧠 Why?

Because we can add **validation logic**

```python
if value < 0:
    print("Invalid marks!")
```

✔ Prevents wrong data input

---

# 🧼 05. Property Decorator

## 📁 05_property_basics.py

### 📘 Explanation:

`@property` is a cleaner way to use getter & setter.

### 🧠 Example:

```python
p.price = 500      # setter
print(p.price)     # getter
```

✔ Looks like normal variable  
✔ Works like method internally

---

# 🧪 Practice Section

---

## 📁 06_practice_bank_account.py

### 📘 What you learn:

✔ Private balance variable  
✔ Deposit & withdraw methods  
✔ Data protection

### 🧠 Concept:

Real-world example of **secure data handling**

---

## 📁 07_practice_user_security.py

### 📘 What you learn:

✔ Hide password using private variable  
✔ Check password safely

### 🧠 Concept:

Basic **authentication system**

---

# 🎯 Day 04 Summary

You Learned:

## 🔐 Access Control

✔ Public variables  
✔ Protected variables (`_var`)  
✔ Private variables (`__var`)

## 🧠 Name Mangling

✔ Python renames private variables internally

## ⚙ Getter & Setter

✔ Safe access to data  
✔ Add validation logic

## 🧼 Property

✔ Cleaner and modern way to manage data

## 🧪 Practice

✔ Bank account system  
✔ User security system

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

