"""
========================================
02_library_service.py
========================================
Service Layer:

✔ Business logic
✔ File handling
"""

from 01_book_model import Book

class Library:
    def __init__(self, file_name="books.txt"):
        self.file_name = file_name

    # Add book
    def add_book(self, book):
        with open(self.file_name, "a") as f:
            f.write(book.to_line())

    # Get all books
    def get_all_books(self):
        books = []
        try:
            with open(self.file_name, "r") as f:
                for line in f:
                    books.append(Book.from_line(line))
        except FileNotFoundError:
            pass
        return books

    # Show books
    def show_books(self):
        books = self.get_all_books()
        if not books:
            print("No books found!")
        for book in books:
            print(book.display())

    # Search book
    def search_book(self, keyword):
        books = self.get_all_books()
        for book in books:
            if keyword.lower() in book.title.lower():
                print(book.display())