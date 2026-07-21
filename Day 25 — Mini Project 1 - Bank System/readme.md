# 🐍 Python OOP – Day 25 — Mini Project 1 - Bank System

---

## 📌 Overview

💡 What is a Bank System in OOP?

A Bank System is a real-world application of Object-Oriented Programming where we simulate banking operations like deposit, withdraw, interest, and account management using classes.

In this project:

- We use **Encapsulation** to protect balance data
- We use **Inheritance** to reuse base account logic
- We use **Method Overriding** for custom behaviors
- We design a **real-world scalable system structure**

👉 Simple idea:

- Account = base blueprint
- SavingsAccount = account + interest
- CurrentAccount = account + overdraft

---

## 📁 01_account_base.py

💡 Base class for all accounts

- Stores user name and balance
- Keeps balance private (encapsulation)
- Provides deposit and withdraw methods

```python id="b1a9k2"
class Account:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance  # private (encapsulation)

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited {amount}"
        return "Invalid deposit amount"

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrawn {amount}"
        return "Insufficient balance"
```

---

## 📁 02_savings_account_inheritance.py

💡 Savings account adds interest feature

- Inherits from Account
- Adds interest calculation

```python id="c8m2dp"
from 01_account_base import Account

class SavingsAccount(Account):
    def __init__(self, name, balance, interest_rate):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.get_balance() * self.interest_rate / 100
        self.deposit(interest)
        return f"Interest added: {interest}"
```

---

## 📁 03_current_account_inheritance.py

💡 Current account supports overdraft

- Allows extra withdrawal beyond balance
- Overrides withdraw method

```python id="p9x4kf"
from 01_account_base import Account

class CurrentAccount(Account):
    def __init__(self, name, balance, overdraft_limit):
        super().__init__(name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.get_balance() + self.overdraft_limit:
            return super().withdraw(amount)
        return "Overdraft limit exceeded"
```

---

## 📁 04_bank_system_main.py

💡 Main program to run the system

- Creates accounts
- Tests deposit, withdraw, interest

```python id="k3m8dn"
from 01_account_base import Account
from 02_savings_account_inheritance import SavingsAccount
from 03_current_account_inheritance import CurrentAccount

acc1 = Account("Monjur", 1000)
print(acc1.deposit(500))
print(acc1.withdraw(300))
print("Balance:", acc1.get_balance())

print("\n--- Savings Account ---\n")

savings = SavingsAccount("Rahim", 2000, 5)
print(savings.add_interest())
print("Balance:", savings.get_balance())

print("\n--- Current Account ---\n")

current = CurrentAccount("Karim", 1000, 500)
print(current.withdraw(1300))
print("Balance:", current.get_balance())
```

---

## 📁 05_encapsulation_demo.py

💡 Encapsulation protects data from direct access

- Balance is hidden using `__balance`
- Only controlled access allowed

```python id="x1n7qp"
class SecureAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def update_balance(self, amount):
        if amount < 0:
            return "Invalid amount"
        self.__balance += amount

acc = SecureAccount(1000)

print(acc.get_balance())
acc.update_balance(500)
print(acc.get_balance())
```

---

## 📁 06_project_structure_note.py

💡 Clean project structure idea

- Each feature in separate file
- Easy to scale and maintain

```python id="m8q2lp"
"""
bank_system/
│
├── account_base.py
├── savings_account.py
├── current_account.py
├── main.py
│
└── README.md
"""
```

---

## 📁 07_feature_extension_example.py

💡 OOP makes system easy to extend

- Add new account types without changing old code

```python id="v3k9sd"
from 01_account_base import Account

class PremiumAccount(Account):
    def bonus(self):
        return "Premium bonus applied!"

acc = PremiumAccount("User", 5000)

print(acc.deposit(1000))
print(acc.bonus())
```

---

## 🎯 Day 25 Summary

- Built a real Bank System using OOP
- Learned Encapsulation for data protection
- Used Inheritance for code reuse
- Practiced Method Overriding
- Understood scalable project structure
- Learned how real backend systems are designed

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

