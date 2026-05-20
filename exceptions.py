"""Custom exception classes for Library Management System"""

class BookNotFoundError(Exception):
    """Raised when a book with given ID is not found"""
    pass

class MemberNotFoundError(Exception):
    """Raised when a member with given ID is not found"""
    pass

class BookUnavailableError(Exception):
    """Raised when attempting to borrow a book that is not available"""
    pass

class LoanNotFoundError(Exception):
    """Raised when a loan with given ID is not found"""
    pass
