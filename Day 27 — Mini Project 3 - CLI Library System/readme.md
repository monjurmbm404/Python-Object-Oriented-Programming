# 🐍 Python OOP – Day 27 — Mini Project 3 - CLI Library System

---

## 📌 Overview

💡 What is a CLI Library System?

A CLI (Command Line Interface) Library System is a simple software where users can add, view, and search books using terminal commands.

This project introduces **real-world backend thinking** using:

- Object-Oriented Programming (OOP)
- File handling (data persistence)
- Clean architecture (Model → Service → UI)

👉 Simple idea:

- Book = data model
- Library = logic + file storage
- CLI = user interaction

---

## 📁 01_book_model.py

💡 Book Model represents a single book

- Stores book information
- Converts object ↔ file format
- Handles data serialization

```python id="b1k9md"
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author

    def to_line(self):
        return f"{self.book_id},{self.title},{self.author}\n"

    @staticmethod
    def from_line(line):
        book_id, title, author = line.strip().split(",")
        return Book(book_id, title, author)

    def display(self):
        return f"[{self.book_id}] {self.title} by {self.author}"
```

---

## 📁 02_library_service.py

💡 Library Service handles business logic

- Adds books to file
- Reads all books
- Searches books

```python id="m8p2kd"
from 01_book_model import Book

class Library:
    def __init__(self, file_name="books.txt"):
        self.file_name = file_name

    def add_book(self, book):
        with open(self.file_name, "a") as f:
            f.write(book.to_line())

    def get_all_books(self):
        books = []
        try:
            with open(self.file_name, "r") as f:
                for line in f:
                    books.append(Book.from_line(line))
        except FileNotFoundError:
            pass
        return books

    def show_books(self):
        books = self.get_all_books()
        if not books:
            print("No books found!")
        for book in books:
            print(book.display())

    def search_book(self, keyword):
        books = self.get_all_books()
        for book in books:
            if keyword.lower() in book.title.lower():
                print(book.display())
```

---

## 📁 03_cli_app.py

💡 CLI Application (User Interface)

- Takes user input
- Calls library methods
- Runs system loop

```python id="c3k8md"
from 01_book_model import Book
from 02_library_service import Library

library = Library()

while True:
    print("\n===== LIBRARY SYSTEM =====")
    print("1. Add Book")
    print("2. Show Books")
    print("3. Search Book")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        book_id = input("Enter ID: ")
        title = input("Enter Title: ")
        author = input("Enter Author: ")

        book = Book(book_id, title, author)
        library.add_book(book)
        print("Book added successfully!")

    elif choice == "2":
        library.show_books()

    elif choice == "3":
        keyword = input("Enter search keyword: ")
        library.search_book(keyword)

    elif choice == "4":
        print("Exiting system...")
        break

    else:
        print("Invalid choice!")
```

---

## 📁 04_file_structure.py

💡 Clean project structure

```python id="s9k2ld"
"""
library_system/
│
├── book_model.py
├── library_service.py
├── cli_app.py
├── books.txt
│
✔ Model → Data
✔ Service → Logic
✔ CLI → User Interface
"""
```

---

## 📁 05_books_sample.txt

💡 Example stored data

```python id="p8m2kd"
1,Python Basics,John
2,OOP Concepts,Alex
3,Data Structures,Mark
```

---

## 🧠 CORE CONCEPTS USED

---

## 🧬 1. OOP Design

- Book → data model
- Library → business logic
- CLI → interface

---

## 💾 2. File Handling

- Data stored in `.txt` file
- Persistent storage system

---

## 🔁 3. Serialization

- Object → string (save)
- String → object (load)

---

## 🧩 4. Layered Architecture

- Model layer (Book)
- Service layer (Library)
- UI layer (CLI)

---

## 🖥️ 5. Real CLI System

- Menu-driven system
- Interactive user input
- Real application behavior

---

## 🚀 WHAT YOU BUILT

✔ Real library management system
✔ Persistent storage using files
✔ Search functionality
✔ Clean OOP architecture
✔ Scalable backend-style design

---

## 🏁 YOU HAVE COMPLETED:

## 📚 Day 27 — Mini Project 3

### You mastered:

- File-based database system
- OOP-based application design
- Serialization & deserialization
- CLI application development
- Clean layered architecture

---

# Author

**Engr. Md Monjur Bakth Mazumder**

🎓 Diploma in Computer Science and Technology — [Moulvibazar Polytechnic Institute](https://mpi.moulvibazar.gov.bd/)  
🎓 BSc in Computer Science & Engineering (CSE) (Ongoing) — [Sylhet International University](https://siu.edu.bd/)

📧 Email: monjurmbm404@gmail.com

### ⭐ If you find this helpful, don’t forget to **star** the repository!
