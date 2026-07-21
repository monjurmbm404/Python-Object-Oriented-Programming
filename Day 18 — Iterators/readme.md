# 🐍 Python OOP – Day 18 — Iterators

---

## 📌 Overview

💡 What is an Iterator?

An **iterator** is an object in Python that lets you go through data **one item at a time** instead of loading everything at once.

In simple words:

- It remembers where it is during looping
- It gives the next value when asked
- It stops automatically when data ends

---

## 🔑 Key Concepts

- `iter()` → creates an iterator from an object
- `next()` → gets the next value
- `__iter__()` → returns the iterator object
- `__next__()` → returns next value
- `StopIteration` → signals end of iteration

---

## 📁 File-by-File Explanation

---

## 📁 01_iterator_basics.py

💡 What is happening here?

This file shows how Python list becomes an iterator using `iter()`.

### 📌 Code Example

```python
numbers = [1, 2, 3]

it = iter(numbers)

print(next(it))
print(next(it))
print(next(it))
```

### 🧠 Explanation

- `iter(numbers)` converts list into iterator
- `next(it)` fetches values one by one
- After last value, it stops automatically

---

## 📁 02_custom_iterator_class.py

💡 Creating your own iterator class

### 📌 Code Example

```python
class MyNumbers:
    def __init__(self):
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 5:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration

obj = MyNumbers()

for num in obj:
    print(num)
```

### 🧠 Explanation

- Class controls its own looping logic
- `__iter__()` returns itself
- `__next__()` generates next value
- Stops after reaching 5 using `StopIteration`

---

## 📁 03_iterator_internal_working.py

💡 How `for loop` works internally

### 📌 Code Example

```python
class Counter:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 3:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration

c = Counter()

it = iter(c)

print(next(it))
print(next(it))
print(next(it))
```

### 🧠 Explanation

- `for loop` internally uses `iter()` + `next()`
- You are manually doing what loop does automatically

---

## 📁 04_iterator_with_data.py

💡 Iterating over internal data list

### 📌 Code Example

```python
class Team:
    def __init__(self, members):
        self.members = members
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.members):
            member = self.members[self.index]
            self.index += 1
            return member
        else:
            raise StopIteration

team = Team(["A", "B", "C"])

for member in team:
    print(member)
```

### 🧠 Explanation

- Class stores a list internally
- Iterator goes through each element step-by-step
- Works like a custom loop engine

---

## 📁 05_iterator_vs_loop.py

💡 Difference between loop and iterator

### 📌 Code Example

```python
nums = [10, 20, 30]

for n in nums:
    print(n)

it = iter(nums)

print(next(it))
print(next(it))
```

### 🧠 Explanation

- `for loop` hides iterator logic
- Manual iterator gives full control
- Useful for custom processing systems

---

## 📁 06_infinite_iterator.py

💡 Infinite iterator concept

### 📌 Code Example

```python
class InfiniteCounter:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        value = self.num
        self.num += 1
        return value
```

### 🧠 Explanation

- No `StopIteration`
- Generates numbers forever
- Used in streaming or live data systems

---

## 📁 07_real_world_iterator.py

💡 Real-world use case (data streaming)

### 📌 Code Example

```python
class DataStream:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1
            return value
        raise StopIteration

stream = DataStream(["User1", "User2", "User3"])

for user in stream:
    print("Processing:", user)
```

### 🧠 Explanation

- Simulates real backend streaming
- Data processed one-by-one
- Memory efficient design

---

## 📁 08_practice_number_iterator.py

💡 Number range iterator

### 📌 Code Example

```python
class Numbers:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.end:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration
```

### 🧠 Explanation

- Custom range generator
- Works like `range()` function
- Fully controlled iteration

---

## 📁 09_practice_even_iterator.py

💡 Even number iterator

### 📌 Code Example

```python
class EvenNumbers:
    def __init__(self, limit):
        self.num = 2
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= self.limit:
            value = self.num
            self.num += 2
            return value
        else:
            raise StopIteration
```

### 🧠 Explanation

- Generates only even numbers
- Skips logic handled inside class
- Useful for filtering streams

---

## 🎯 Day 18 Summary

- Learned what iterators are internally
- Understood `iter()` and `next()` functions
- Built custom iterator classes
- Learned `StopIteration` behavior
- Compared loop vs iterator system
- Created real-world streaming-style iterator
- Practiced range and even number iterators

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

