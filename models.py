"""Data models for Library Management System"""
from datetime import datetime

class Book:
    """Represents a book in the library"""
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True
    
    def borrow(self):
        """Mark book as borrowed"""
        self.available = False
    
    def return_book(self):
        """Mark book as returned"""
        self.available = True
    
    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"{self.book_id} - {self.title} by {self.author} [{status}]"

class Member:
    """Represents a library member"""
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email
    
    def __str__(self):
        return f"{self.member_id} - {self.name} ({self.email})"

class Loan:
    """Represents a book loan transaction"""
    def __init__(self, loan_id, book, member):
        self.loan_id = loan_id
        self.book = book
        self.member = member
        self.issue_date = datetime.now()
        self.return_date = None
        self.is_active = True
    
    def close_loan(self):
        """Mark loan as closed/returned"""
        self.return_date = datetime.now()
        self.is_active = False
    
    def __str__(self):
        status = "Active" if self.is_active else "Closed"
        return f"{self.loan_id} - {self.member.name} borrowed {self.book.title} [{status}]"
