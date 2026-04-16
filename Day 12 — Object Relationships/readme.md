# 🐍 Python OOP – Day 12: Object Relationships

---

## 📌 Overview

In this day, you will learn how **objects interact with each other** in real-world programs 🤝

Object relationships are very important because:

- They help you design real-world systems
- They make your code more flexible and reusable
- They improve your problem-solving skills in OOP

---

## 💡 What are Object Relationships?

In OOP, classes and objects don’t work alone. They **connect and interact** in different ways.

Main types of relationships:

- 🔗 **Association** → "uses-a"
- 🧩 **Aggregation** → weak "has-a"
- 🏗 **Composition** → strong "has-a"

---

# 🔗 01. Association (uses-a)

## 📁 01_association_basic.py

### 📘 Explanation:

Association means:

- One object **uses another object**
- Both objects are **independent**
- No ownership

### 🧠 Example:

```python
class Teacher:
    def __init__(self, name):
        self.name = name

    def teach(self):
        print(self.name, "is teaching")

class Student:
    def __init__(self, name):
        self.name = name

    def learn(self, teacher):
        print(self.name, "is learning from", teacher.name)
        teacher.teach()

t = Teacher("Mr. Rahman")
s = Student("Monjur")

s.learn(t)
```

### 🧠 Key Points:

- 🔹 Student uses Teacher
- 🔹 Both exist independently
- 🔹 Relationship is temporary

---

# 🔗 02. Association with Multiple Objects

## 📁 02_association_multiple_objects.py

### 📘 Explanation:

- One object can interact with multiple objects

### 🧠 Example:

```python
class Driver:
    def drive(self):
        print("Driving vehicle")

class Car:
    def start(self):
        print("Car started")

class Person:
    def use(self, driver, car):
        driver.drive()
        car.start()
        print("Person is traveling")
```

### 🧠 Key Points:

- 🔹 No ownership
- 🔹 Objects just collaborate

---

# 🧩 03. Aggregation (Weak has-a)

## 📁 03_aggregation_basic.py

### 📘 Explanation:

Aggregation means:

- One class **has another class**
- But the child object can exist **independently**

### 🧠 Example:

```python
class Teacher:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, teachers):
        self.teachers = teachers

    def show_teachers(self):
        for t in self.teachers:
            print(t.name)

t1 = Teacher("A")
t2 = Teacher("B")

dept = Department([t1, t2])
dept.show_teachers()
```

### 🧠 Key Points:

- 🔹 Department has Teachers
- 🔹 Teachers can exist without Department

---

# ⚖️ 04. Aggregation vs Composition

## 📁 04_aggregation_vs_composition.py

### 📘 Explanation:

| Feature    | Aggregation | Composition |
| ---------- | ----------- | ----------- |
| Ownership  | Weak        | Strong      |
| Dependency | Low         | High        |
| Lifecycle  | Independent | Dependent   |

### 🧠 Example (Aggregation):

```python
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self, engine):
        self.engine = engine  # external object
```

---

# 🏗 05. Composition (Strong has-a)

## 📁 05_composition_deep.py

### 📘 Explanation:

Composition means:

- Object is **created inside another object**
- Strong ownership
- Cannot exist independently

### 🧠 Example:

```python
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()  # created inside

    def start(self):
        self.engine.start()
        print("Car running")

c = Car()
c.start()
```

### 🧠 Key Points:

- 🔹 Car owns Engine
- 🔹 Engine depends on Car

---

# 🔄 06. Composition Lifecycle

## 📁 06_composition_lifecycle.py

### 📘 Explanation:

- If parent is destroyed → child is also destroyed

### 🧠 Example:

```python
class Heart:
    def beat(self):
        print("Heart beating")

class Human:
    def __init__(self):
        self.heart = Heart()

    def live(self):
        self.heart.beat()
        print("Human alive")
```

### 🧠 Key Points:

- 🔹 Strong dependency
- 🔹 Same lifecycle

---

# 🌍 07. Real-World Example

## 📁 07_real_world_relationships.py

### 📘 Explanation:

- Combines aggregation + composition

### 🧠 Example:

```python
class Student:
    def __init__(self, name):
        self.name = name

class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

class School:
    def __init__(self):
        self.classroom = Classroom()
```

### 🧠 Key Points:

- 🔹 School → Composition (owns classroom)
- 🔹 Classroom → Aggregation (has students)

---

# 🧪 Practice Section

---

## 📁 08_practice_company_system.py

### 📘 Task:

- Create Company
- Add Employees
- Show employee list

---

## 📁 09_practice_composition_system.py

### 📘 Task:

- Create Computer
- Use CPU inside it
- Run system

---

# 🎯 Day 12 Summary

## 🔗 Association

- 🔹 uses-a relationship
- 🔹 no ownership
- 🔹 independent objects

## 🧩 Aggregation

- 🔹 weak has-a
- 🔹 child exists independently
- 🔹 flexible design

## 🏗 Composition

- 🔹 strong has-a
- 🔹 child depends on parent
- 🔹 tight relationship

## 🧠 Design Understanding

- 🔹 how objects interact
- 🔹 when to use which relationship
- 🔹 real-world system modeling

---

# Author

**Engr. Md Monjur Bakth Mazumder**

🎓 Diploma in Computer Science and Technology — [Moulvibazar Polytechnic Institute](https://mpi.moulvibazar.gov.bd/)  
🎓 BSc in Computer Science & Engineering (CSE) (Ongoing) — [Sylhet International University](https://siu.edu.bd/)

📧 Email: monjurmbm404@gmail.com

### ⭐ If you find this helpful, don’t forget to **star** the repository!
