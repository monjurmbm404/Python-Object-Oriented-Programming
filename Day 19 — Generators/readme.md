# 🐍 Python OOP – Day 19 — Generators

---

## 📌 Overview

💡 What is a Generator?

A **generator** is a special type of function in Python that produces values **one at a time instead of storing everything in memory**.

Unlike normal functions, generators use:

- `yield` → to return a value temporarily
- `next()` → to get the next value
- Lazy evaluation → values are created only when needed

👉 In simple words:

- Normal function → gives everything at once
- Generator → gives one item at a time

---

## 🔑 Key Concepts

- `yield` → pauses function and remembers state
- `next()` → resumes execution from last `yield`
- Lazy evaluation → memory efficient processing
- Infinite generator → produces unlimited values safely
- Pipeline → chaining multiple generators

---

## 📁 File-by-File Explanation

---

## 📁 01_generator_basics.py

💡 Basic idea of generator

### 📌 Code Example

```python id="0wq7xk"
def simple_generator():
    yield 1
    yield 2
    yield 3

gen = simple_generator()

print(next(gen))
print(next(gen))
print(next(gen))
```

### 🧠 Explanation

- Each `yield` returns a value step by step
- Function does not end after first yield
- It remembers last position

---

## 📁 02_generator_vs_function.py

💡 Difference between normal function and generator

### 📌 Code Example

```python id="k3m1qv"
def normal_function():
    return [1, 2, 3]

def generator_function():
    yield 1
    yield 2
    yield 3

print(normal_function())

for value in generator_function():
    print(value)
```

### 🧠 Explanation

- `return` → gives full list at once
- `yield` → gives one value at a time
- Generator is more memory efficient

---

## 📁 03_lazy_evaluation.py

💡 Lazy evaluation concept

### 📌 Code Example

```python id="x9p2aa"
def numbers():
    for i in range(1, 6):
        print("Generating:", i)
        yield i

gen = numbers()

print(next(gen))
print(next(gen))
```

### 🧠 Explanation

- Values are generated only when needed
- Execution pauses after each yield
- Useful for large data processing

---

## 📁 04_generator_in_class.py

💡 Generator inside class (OOP style)

### 📌 Code Example

```python id="v8q1lm"
class NumberSeries:
    def __init__(self, limit):
        self.limit = limit

    def generate(self):
        for i in range(1, self.limit + 1):
            yield i

obj = NumberSeries(5)

for num in obj.generate():
    print(num)
```

### 🧠 Explanation

- Class method returns generator
- Clean OOP + generator combination
- Used in real backend systems

---

## 📁 05_generator_memory_efficiency.py

💡 Memory saving advantage

### 📌 Code Example

```python id="m1n7zp"
def big_data():
    for i in range(1, 1000000):
        yield i

gen = big_data()

print(next(gen))
print(next(gen))
```

### 🧠 Explanation

- Does NOT store full list in memory
- Generates values one-by-one
- Perfect for big data systems

---

## 📁 06_generator_pipeline.py

💡 Pipeline processing using generators

### 📌 Code Example

```python id="p3r8tt"
def read_data():
    for i in range(5):
        yield i

def square(data):
    for i in data:
        yield i * i

def filter_even(data):
    for i in data:
        if i % 2 == 0:
            yield i

data = read_data()
squared = square(data)
filtered = filter_even(squared)

for value in filtered:
    print(value)
```

### 🧠 Explanation

- Multiple generators connected together
- Data flows step-by-step
- Used in real ETL pipelines

---

## 📁 07_infinite_generator.py

💡 Infinite generator concept

### 📌 Code Example

```python id="f2k9ab"
def infinite_counter():
    i = 1
    while True:
        yield i
        i += 1

gen = infinite_counter()

print(next(gen))
print(next(gen))
print(next(gen))
```

### 🧠 Explanation

- Generates values forever
- No memory limit
- Must control usage carefully

---

## 📁 08_real_world_generator.py

💡 Real-world file streaming

### 📌 Code Example

```python id="t7w2yy"
def read_lines(file_path):
    with open(file_path, "r") as file:
        for line in file:
            yield line.strip()
```

### 🧠 Explanation

- Reads file line by line
- Does not load full file into memory
- Used in logs and big files processing

---

## 📁 09_practice_even_generator.py

💡 Even number generator

### 📌 Code Example

```python id="e9m1qq"
def even_numbers(limit):
    for i in range(2, limit + 1, 2):
        yield i

for num in even_numbers(10):
    print(num)
```

### 🧠 Explanation

- Generates only even numbers
- Uses `yield` instead of list

---

## 📁 10_practice_fibonacci_generator.py

💡 Fibonacci sequence generator

### 📌 Code Example

```python id="f7n3kk"
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(10):
    print(num)
```

### 🧠 Explanation

- Generates Fibonacci numbers one by one
- Efficient compared to storing list

---

## 🎯 Day 19 Summary

- Learned what generators are in Python
- Understood `yield` vs `return`
- Explored lazy evaluation concept
- Built class-based generators
- Learned memory-efficient programming
- Created infinite generators
- Built real-world pipeline systems
- Practiced Fibonacci and even number generators

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

