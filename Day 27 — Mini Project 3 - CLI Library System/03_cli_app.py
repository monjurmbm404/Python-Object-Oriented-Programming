"""
========================================
03_cli_app.py
========================================
CLI Interface:

✔ User interaction layer
✔ Connects everything
"""

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