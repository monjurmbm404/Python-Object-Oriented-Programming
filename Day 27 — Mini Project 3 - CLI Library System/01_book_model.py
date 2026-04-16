"""
========================================
01_book_model.py
========================================
Book Model:

✔ Represents a single book
✔ Pure data class (OOP model)
"""

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author

    def to_line(self):
        # Convert object → string for file storage
        return f"{self.book_id},{self.title},{self.author}\n"

    @staticmethod
    def from_line(line):
        # Convert file line → object
        book_id, title, author = line.strip().split(",")
        return Book(book_id, title, author)

    def display(self):
        return f"[{self.book_id}] {self.title} by {self.author}"