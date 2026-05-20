# 📚 Library Management System

A comprehensive Python-based Library Management System that allows users to manage books, members, and loans efficiently.

## Features

The system supports 8 main operations:

1. **➕ Add Book** - Register new books to the library catalog
2. **👤 Register Member** - Register new library members
3. **📖 Borrow Book** - Members can borrow books with validation
4. **🔄 Return Book** - Process book returns and close loans
5. **📚 View Books** - Display all books with availability status
6. **👥 View Members** - Display all registered members
7. **📋 View Loans** - Display all active and closed loans
8. **👋 Exit** - Exit the program

## Project Structure

```
Library-Management-System/
├── main.py                 # Interactive CLI interface
├── library_service.py      # Business logic layer
├── models.py              # Data models (Book, Member, Loan)
├── exceptions.py          # Custom exceptions
└── README.md             # This file
```

## Data Models

### Book
- `book_id`: Unique identifier
- `title`: Book title
- `author`: Book author
- `available`: Boolean flag (True = available, False = borrowed)

### Member
- `member_id`: Unique identifier
- `name`: Member name
- `email`: Member email

### Loan
- `loan_id`: Unique identifier (format: L001, L002, etc.)
- `book`: Reference to Book object
- `member`: Reference to Member object
- `issue_date`: Date when book was borrowed
- `return_date`: Date when book was returned (null if still active)
- `is_active`: Boolean flag (True = active, False = closed)

## Usage

### Running the Program

```bash
python main.py
```

### Example Workflow

```
1. Add Book
   - Enter Book ID: B001
   - Enter Book Title: Python Programming
   - Enter Book Author: John Doe
   ✅ Book added: 'Python Programming'

2. Register Member
   - Enter Member ID: M001
   - Enter Member Name: Jane Smith
   - Enter Member Email: jane@example.com
   ✅ Member registered: Jane Smith

3. Borrow Book
   - Enter Book ID: B001
   - Enter Member ID: M001
   ✅ Jane Smith borrowed 'Python Programming'
      Loan ID: L001

4. View Loans
   - Shows: L001 - Jane Smith borrowed Python Programming [Active]

5. Return Book
   - Enter Loan ID: L001
   ✅ Jane Smith returned 'Python Programming'
      Loan ID: L001 [CLOSED]

6. View Loans
   - Shows: L001 - Jane Smith borrowed Python Programming [Closed]
```

## Error Handling

The system includes comprehensive error handling:

- **BookNotFoundError**: Raised when a book ID doesn't exist
- **MemberNotFoundError**: Raised when a member ID doesn't exist
- **BookUnavailableError**: Raised when trying to borrow an already borrowed book
- **LoanNotFoundError**: Raised when a loan ID doesn't exist

## Architecture

### Layered Architecture

1. **Presentation Layer** (`main.py`)
   - User interface with interactive menu
   - Input validation
   - User-friendly output

2. **Business Logic Layer** (`library_service.py`)
   - Core operations (add, borrow, return, view)
   - Data validation
   - Error handling

3. **Data Layer** (`models.py`)
   - Data models and their relationships
   - Object representations

4. **Exception Layer** (`exceptions.py`)
   - Custom exceptions for specific errors

## Features Flowchart Reference

Each feature follows the detailed flowchart specification:

- ✅ Add Book - Simple creation flow
- ✅ Register Member - Simple registration flow
- ✅ Borrow Book - Includes validation for book, member, and availability
- ✅ Return Book - Finds and closes loans
- ✅ View Books - Displays with availability status
- ✅ View Members - Displays member details
- ✅ View Loans - Shows active and closed loans
- ✅ Exit - Gracefully terminates the program

## Requirements

- Python 3.6 or higher
- No external dependencies required

## License

This project is open source and available under the MIT License.

## Author

Created as a mini project for Library Management System demonstration.
