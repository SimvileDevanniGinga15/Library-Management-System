"""Business logic layer for Library Management System"""
from models import Book, Member, Loan
from exceptions import (
    BookNotFoundError,
    MemberNotFoundError,
    BookUnavailableError,
    LoanNotFoundError
)
from datetime import datetime

class LibraryService:
    """Service class to manage library operations"""
    
    def __init__(self):
        self._books = {}  # Dictionary to store books
        self._members = {}  # Dictionary to store members
        self._loans = []  # List to store loans
        self._loan_counter = 0  # Counter for generating loan IDs
    
    def add_book(self, book_id, title, author):
        """
        Add a new book to the library
        
        Args:
            book_id: Unique book identifier
            title: Book title
            author: Book author
        
        Returns:
            Book object created
        """
        book = Book(book_id, title, author)
        self._books[book_id] = book
        return book
    
    def register_member(self, member_id, name, email):
        """
        Register a new member to the library
        
        Args:
            member_id: Unique member identifier
            name: Member name
            email: Member email
        
        Returns:
            Member object created
        """
        member = Member(member_id, name, email)
        self._members[member_id] = member
        return member
    
    def borrow_book(self, book_id, member_id):
        """
        Process book borrowing
        
        Args:
            book_id: ID of book to borrow
            member_id: ID of member borrowing
        
        Returns:
            Loan object created
        
        Raises:
            BookNotFoundError: If book doesn't exist
            MemberNotFoundError: If member doesn't exist
            BookUnavailableError: If book is already borrowed
        """
        # Check if book exists
        book = self._books.get(book_id)
        if book is None:
            raise BookNotFoundError(f"Book with ID {book_id} not found.")
        
        # Check if member exists
        member = self._members.get(member_id)
        if member is None:
            raise MemberNotFoundError(f"Member with ID {member_id} not found.")
        
        # Check if book is available
        if not book.available:
            raise BookUnavailableError(f"Book '{book.title}' is already borrowed.")
        
        # Create loan
        self._loan_counter += 1
        loan_id = f"L{self._loan_counter:03d}"
        loan = Loan(loan_id, book, member)
        
        # Mark book as borrowed
        book.borrow()
        
        # Add loan to list
        self._loans.append(loan)
        
        return loan
    
    def return_book(self, loan_id):
        """
        Process book return
        
        Args:
            loan_id: ID of the loan to close
        
        Returns:
            Loan object updated
        
        Raises:
            LoanNotFoundError: If loan doesn't exist
        """
        # Find the loan
        loan = None
        for l in self._loans:
            if l.loan_id == loan_id:
                loan = l
                break
        
        if loan is None:
            raise LoanNotFoundError(f"Loan with ID {loan_id} not found.")
        
        # Mark book as available
        loan.book.return_book()
        
        # Close the loan
        loan.close_loan()
        
        return loan
    
    def view_books(self):
        """
        Get all books in the library
        
        Returns:
            List of Book objects
        """
        return list(self._books.values())
    
    def view_members(self):
        """
        Get all registered members
        
        Returns:
            List of Member objects
        """
        return list(self._members.values())
    
    def view_loans(self):
        """
        Get all loans
        
        Returns:
            List of Loan objects
        """
        return list(self._loans)
    
    def get_book(self, book_id):
        """
        Get a specific book by ID
        
        Args:
            book_id: ID of book to retrieve
        
        Returns:
            Book object or None
        """
        return self._books.get(book_id)
    
    def get_member(self, member_id):
        """
        Get a specific member by ID
        
        Args:
            member_id: ID of member to retrieve
        
        Returns:
            Member object or None
        """
        return self._members.get(member_id)
