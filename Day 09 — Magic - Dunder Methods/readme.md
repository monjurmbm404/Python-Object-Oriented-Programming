# 🐍 Python OOP – Day 09: Magic / Dunder Methods

---

## 📌 Overview

Welcome to **Day 09 of Python OOP** 🚀

Today you will learn **Magic Methods (also called Dunder Methods)** in Python.

These are special methods that start and end with `__` (double underscores).

You will understand how to:

✔ Customize built-in functions like `print()` and `len()`  
✔ Overload operators like `+`, `==`  
✔ Control object behavior in Python  
✔ Make classes behave like built-in types

---

## 💡 What are Magic / Dunder Methods?

**Dunder methods = “Double Underscore methods”**

👉 Example: `__str__`, `__len__`, `__add__`

### 🧠 Simple Idea:

Python allows you to **change how operators and functions behave for your objects**.

---

## 🎯 Why Magic Methods are Important?

✔ Make custom classes behave like built-in types  
✔ Improve readability and usability  
✔ Enable operator overloading  
✔ Used in real-world frameworks and libraries

---

# 🧾 01. `__str__` vs `__repr__`

## 📁 01_str_vs_repr.py

### 📘 Explanation:

| Method     | Purpose                |
| ---------- | ---------------------- |
| `__str__`  | User-friendly output   |
| `__repr__` | Developer/debug output |

### 🧠 Example:

```python id="magic1"
print(student)        # uses __str__
print(repr(student))  # uses __repr__
```

### 🔑 Key Idea:

✔ `__str__` → readable for users  
✔ `__repr__` → detailed for developers

---

# 📏 02. `__len__`

## 📁 02_len_method.py

### 📘 Explanation:

Defines behavior of:

👉 `len(object)`

### 🧠 Example:

```python id="magic2"
len(team)
```

### 🔑 Key Idea:

✔ You decide what “length” means for your object

---

# ➕ 03. `__add__` (Operator Overloading)

## 📁 03_add_operator_overloading.py

### 📘 Explanation:

Allows you to customize:

👉 `+` operator behavior

### 🧠 Example:

```python id="magic3"
result = n1 + n2
```

### 🔑 Key Idea:

✔ You can add custom objects like numbers

---

# ⚖ 04. `__eq__` (Comparison)

## 📁 04_eq_comparison.py

### 📘 Explanation:

Defines behavior of:

👉 `==` operator

### 🧠 Example:

```python id="magic4"
p1 == p2
```

### 🔑 Key Idea:

✔ You control how objects are compared

---

# 🧮 05. Operator Overloading (Vector Example)

## 📁 05_operator_overloading_basic.py

### 📘 Explanation:

You can define math-like behavior for objects.

### 🧠 Example:

```python id="magic5"
v3 = v1 + v2
```

### 🔑 Key Idea:

✔ Objects behave like mathematical vectors

---

# 🔗 06. Combined Dunder Methods

## 📁 06_len_add_eq_combined.py

### 📘 Explanation:

You can combine multiple magic methods in one class.

### 🧠 Example:

```python id="magic6"
len(box)
box1 + box2
box1 == box2
```

### 🔑 Key Idea:

✔ One class → multiple custom behaviors

---

# 🌍 07. Real-World Example (Money System)

## 📁 07_real_world_operator_overloading.py

### 📘 Explanation:

Money objects behave like real numbers.

### 🧠 Example:

```python id="magic7"
total = m1 + m2
```

### 🔑 Key Idea:

✔ Makes real-world systems more natural

---

# 🧪 Practice Section

---

## 📁 08_practice_student_system.py

### 📘 What you learn:

✔ Add student marks using `+` operator

### 🧠 Example:

```python id="magic8"
s3 = s1 + s2
```

✔ Automatically sums marks

---

## 📁 09_practice_cart_system.py

### 📘 What you learn:

✔ Shopping cart behavior  
✔ Length + merging carts

### 🧠 Example:

```python id="magic9"
len(cart)
cart1 + cart2
```

✔ Works like real shopping systems

---

# 🎯 Day 09 Summary

You Learned:

## 🪄 Magic Methods

✔ Special methods starting with `__`

## 🧾 Object Display

✔ `__str__` → user-friendly  
✔ `__repr__` → debug-friendly

## 📏 Built-in Function Control

✔ `__len__` → len() behavior

## ➕ Operator Overloading

✔ `__add__` → + operator  
✔ `__eq__` → == operator

## 🌍 Real-world Usage

✔ Money systems  
✔ Cart systems  
✔ Mathematical objects

---

# Author

**Engr. Md Monjur Bakth Mazumder**

🎓 Diploma in Computer Science and Technology — [Moulvibazar Polytechnic Institute](https://mpi.moulvibazar.gov.bd/)  
🎓 BSc in Computer Science & Engineering (CSE) (Ongoing) — [Sylhet International University](https://siu.edu.bd/)

📧 Email: monjurmbm404@gmail.com

### ⭐ If you find this helpful, don’t forget to **star** the repository!
