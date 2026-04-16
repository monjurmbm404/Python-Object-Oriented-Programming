# 🐍 Python OOP – Day 24 — Testing OOP Code

---

## 📌 Overview

💡 What is Testing in OOP?

Testing in Object-Oriented Programming means checking whether your classes and methods work correctly. Instead of guessing, you write small test cases to verify your logic.

- Ensures your code works as expected
- Helps catch bugs early
- Makes your code reliable and professional
- Important for real-world backend development

👉 Simple example:

```python
def add(a, b):
    return a + b

# Testing
print(add(2, 3) == 5)  # True
```

---

## 📁 01_testing_mindset.py

💡 Testing mindset means writing code that is easy to test

- Test behavior, not internal code
- Keep functions small
- Predictable output

```python
def add(a, b):
    return a + b

# Manual test
print(add(2, 3) == 5)  # True
```

---

## 📁 02_bad_vs_good_design.py

💡 Good design makes testing easy

- Bad: tightly coupled (hard to test)
- Good: flexible and testable

```python
# ❌ BAD
class Payment:
    def process(self):
        print("Connecting to real bank...")
        return True

# ✔ GOOD
class Payment:
    def __init__(self, gateway):
        self.gateway = gateway

    def process(self):
        return self.gateway.pay()
```

---

## 📁 03_dependency_injection_test.py

💡 Dependency Injection helps replace real systems with fake ones for testing

- Makes testing easier
- No real API/database needed

```python
class FakeGateway:
    def pay(self):
        return True

class Payment:
    def __init__(self, gateway):
        self.gateway = gateway

    def process(self):
        return self.gateway.pay()

payment = Payment(FakeGateway())

print(payment.process())  # True
```

---

## 📁 04_simple_unit_test.py

💡 Unit Testing means testing small parts of code

- One function at a time
- Simple and focused

```python
def multiply(a, b):
    return a * b

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(0, 5) == 0

test_multiply()
print("All tests passed")
```

---

## 📁 05_testing_class_methods.py

💡 You can test class methods just like functions

```python
class Calculator:
    def add(self, a, b):
        return a + b

def test_calculator():
    calc = Calculator()
    assert calc.add(2, 3) == 5

test_calculator()
print("Calculator test passed")
```

---

## 📁 06_edge_case_testing.py

💡 Always test edge cases (unexpected inputs)

- Zero
- Empty data
- Invalid input

```python
def divide(a, b):
    if b == 0:
        return None
    return a / b

def test_divide():
    assert divide(10, 2) == 5
    assert divide(10, 0) is None

test_divide()
print("Divide tests passed")
```

---

## 📁 07_testable_class_design.py

💡 Write classes that return values instead of printing

- Easier to test
- Cleaner design

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

def test_bank():
    acc = BankAccount(1000)
    assert acc.deposit(500) == 1500

test_bank()
print("Bank test passed")
```

---

## 📁 08_real_world_testing.py

💡 Test real business logic

```python
class Discount:
    def apply(self, price):
        return price * 0.9

def test_discount():
    d = Discount()
    assert d.apply(1000) == 900

test_discount()
print("Discount test passed")
```

---

## 📁 09_testing_summary_example.py

💡 Combine everything in one example

```python
class Cart:
    def total(self, prices):
        return sum(prices)

def test_cart():
    cart = Cart()
    assert cart.total([100, 200, 300]) == 600
    assert cart.total([]) == 0

test_cart()
print("Cart tests passed")
```

---

## 🎯 Day 24 Summary

- Testing ensures code correctness
- Write small, testable functions
- Use dependency injection for flexibility
- Practice unit testing
- Always check edge cases
- Clean code = easy testing

---

# Author

**Engr. Md Monjur Bakth Mazumder**

🎓 Diploma in Computer Science and Technology — [Moulvibazar Polytechnic Institute](https://mpi.moulvibazar.gov.bd/)  
🎓 BSc in Computer Science & Engineering (CSE) (Ongoing) — [Sylhet International University](https://siu.edu.bd/)

📧 Email: monjurmbm404@gmail.com

### ⭐ If you find this helpful, don’t forget to **star** the repository!
