# 🐍 Python OOP – Day 17: Exception Handling in OOP

---

## 📌 Overview

💡 **What is Exception Handling in OOP?**

Exception handling is a way to **prevent program crashes when errors happen** during object-oriented programming.

In OOP, exceptions are used inside:

- Classes
- Methods
- Object validation
- Business logic (banking, ecommerce, etc.)

👉 Instead of breaking the program, we **catch errors and handle them safely**.

---

## 🎯 Why Exception Handling in OOP?

- Prevent system crashes
- Make classes safer and more reliable
- Validate user input inside objects
- Create custom error rules
- Build real-world systems (bank, payment, etc.)

---

# 📁 01_exceptions_inside_class.py

```python id="e1"
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        try:
            if amount > self.balance:
                raise ValueError("Insufficient balance")
            self.balance -= amount
            print("Withdrawal successful:", amount)

        except ValueError as e:
            print("Error:", e)

acc = BankAccount(1000)

acc.withdraw(500)
acc.withdraw(2000)
```

### 💡 Explanation:

- Error handled inside class method
- Prevents program crash
- Uses `raise` to trigger custom error

---

# 📁 02_custom_exception.py

```python id="e2"
class InvalidAgeError(Exception):
    pass

class Person:
    def __init__(self, name, age):
        if age < 0:
            raise InvalidAgeError("Age cannot be negative")
        self.name = name
        self.age = age

try:
    p = Person("Monjur", -5)
except InvalidAgeError as e:
    print("Custom Error:", e)
```

### 💡 Explanation:

- Custom exceptions let you define your own rules
- Useful for validation systems
- Cleaner and more readable error handling

---

# 📁 03_custom_exception_with_class_logic.py

```python id="e3"
class InsufficientBalanceError(Exception):
    pass

class Account:
    def __init__(self, balance):
        self.balance = balance

    def transfer(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError("Not enough balance for transfer")

        self.balance -= amount
        print("Transfer successful:", amount)

acc = Account(1000)

try:
    acc.transfer(1500)
except InsufficientBalanceError as e:
    print("Transaction Failed:", e)
```

### 💡 Explanation:

- Business logic uses custom exceptions
- Perfect for banking systems
- Separates normal logic and error logic

---

# 📁 04_robust_class_design.py

```python id="e4"
class Product:
    def __init__(self, name, price):
        if price < 0:
            raise ValueError("Price cannot be negative")

        self.name = name
        self.price = price

    def apply_discount(self, percent):
        if percent < 0 or percent > 100:
            raise ValueError("Invalid discount percentage")

        self.price -= (self.price * percent) / 100

p = Product("Laptop", 50000)

try:
    p.apply_discount(10)
    print(p.price)

    p.apply_discount(200)
except ValueError as e:
    print("Error:", e)
```

### 💡 Explanation:

- Validates data before processing
- Ensures object always stays in correct state

---

# 📁 05_exception_in_methods.py

```python id="e5"
class Calculator:
    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            print("Cannot divide by zero")
            return None

calc = Calculator()

print(calc.divide(10, 2))
print(calc.divide(10, 0))
```

### 💡 Explanation:

- Each method handles its own error
- Prevents crashing during invalid operations

---

# 📁 06_multiple_exceptions_class.py

```python id="e6"
class DataProcessor:
    def process(self, data):
        try:
            number = int(data)
            result = 100 / number
            print("Result:", result)

        except ValueError:
            print("Invalid input: not a number")

        except ZeroDivisionError:
            print("Cannot divide by zero")

dp = DataProcessor()

dp.process("10")
dp.process("abc")
dp.process("0")
```

### 💡 Explanation:

- Multiple error types handled separately
- Each error has different meaning

---

# 📁 07_exception_with_validation.py

```python id="e7"
class User:
    def __init__(self, username, age):
        if len(username) < 3:
            raise ValueError("Username too short")

        if age < 0:
            raise ValueError("Invalid age")

        self.username = username
        self.age = age

try:
    u = User("ab", 20)
except ValueError as e:
    print("Validation Error:", e)
```

### 💡 Explanation:

- Input validation inside constructor
- Prevents invalid object creation

---

# 📁 08_real_world_exception_system.py

```python id="e8"
class TransactionError(Exception):
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise TransactionError("Deposit must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise TransactionError("Insufficient balance")
        self.balance -= amount

acc = BankAccount(1000)

try:
    acc.deposit(500)
    acc.withdraw(2000)
except TransactionError as e:
    print("Bank Error:", e)
```

### 💡 Explanation:

- Real banking system logic
- Strong validation using custom exception
- Safe transaction handling

---

# 📁 09_practice_safe_system.py

```python id="e9"
class SafeSystem:
    def __init__(self, data):
        self.data = data

    def get_item(self, index):
        try:
            return self.data[index]
        except IndexError:
            return "Invalid index"

system = SafeSystem([10, 20, 30])

print(system.get_item(1))
print(system.get_item(10))
```

### 💡 Explanation:

- Safe access to data
- Prevents index crash
- Returns fallback value instead

---

# 🎯 Day 17 Summary

Today you learned:

- 🚨 Exception handling inside classes
- 🧠 Custom exceptions for real-world rules
- 🏗 Robust class design with validation
- ⚙ Handling multiple error types
- 🏦 Real-world banking safety logic
- 🔐 Building crash-safe OOP systems

---

# Author

**Engr. Md Monjur Bakth Mazumder**

🎓 Diploma in Computer Science and Technology — [Moulvibazar Polytechnic Institute](https://mpi.moulvibazar.gov.bd/)  
🎓 BSc in Computer Science & Engineering (CSE) (Ongoing) — [Sylhet International University](https://siu.edu.bd/)

📧 Email: monjurmbm404@gmail.com

### ⭐ If you find this helpful, don’t forget to **star** the repository!
