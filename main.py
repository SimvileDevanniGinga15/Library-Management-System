"""Main entry point for Library Management System"""
from library_service import LibraryService
from exceptions import (
    BookNotFoundError,
    MemberNotFoundError,
    BookUnavailableError,
    LoanNotFoundError
)

def main():
    """Main function to run the library management system"""
    service = LibraryService()
    
    print("\n" + "="*60)
    print("📚 LIBRARY MANAGEMENT SYSTEM 📚".center(60))
    print("="*60 + "\n")
    
    while True:
        # Display menu
        print("\n" + "-"*60)
        print("MAIN MENU".center(60))
        print("-"*60)
        print("1. ➕  Add Book")
        print("2. 👤  Register Member")
        print("3. 📖  Borrow Book")
        print("4. 🔄  Return Book")
        print("5. 📚  View Books")
        print("6. 👥  View Members")
        print("7. 📋  View Loans")
        print("8. 👋  Exit")
        print("-"*60)
        
        choice = input("\nEnter your choice (1-8): ").strip()
        
        try:
            if choice == "1":
                # Add Book
                print("\n--- Add Book ---")
                book_id = input("Enter Book ID: ").strip()
                title = input("Enter Book Title: ").strip()
                author = input("Enter Book Author: ").strip()
                
                service.add_book(book_id, title, author)
                print(f"\n✅ Book added: '{title}'")
            
            elif choice == "2":
                # Register Member
                print("\n--- Register Member ---")
                member_id = input("Enter Member ID: ").strip()
                name = input("Enter Member Name: ").strip()
                email = input("Enter Member Email: ").strip()
                
                service.register_member(member_id, name, email)
                print(f"\n✅ Member registered: {name}")
            
            elif choice == "3":
                # Borrow Book
                print("\n--- Borrow Book ---")
                book_id = input("Enter Book ID: ").strip()
                member_id = input("Enter Member ID: ").strip()
                
                try:
                    loan = service.borrow_book(book_id, member_id)
                    print(f"\n✅ {loan.member.name} borrowed '{loan.book.title}'")
                    print(f"   Loan ID: {loan.loan_id}")
                except (BookNotFoundError, MemberNotFoundError, BookUnavailableError) as e:
                    print(f"\n❌ Error: {e}")
            
            elif choice == "4":
                # Return Book
                print("\n--- Return Book ---")
                loan_id = input("Enter Loan ID: ").strip()
                
                try:
                    loan = service.return_book(loan_id)
                    print(f"\n✅ {loan.member.name} returned '{loan.book.title}'")
                    print(f"   Loan ID: {loan.loan_id} [CLOSED]")
                except LoanNotFoundError as e:
                    print(f"\n❌ Error: {e}")
            
            elif choice == "5":
                # View Books
                print("\n--- View Books ---")
                books = service.view_books()
                
                if not books:
                    print("\n📭 No books found.")
                else:
                    print(f"\n📚 Books ({len(books)} total):")
                    print("-" * 60)
                    for book in books:
                        print(f"   {book}")
                    print("-" * 60)
            
            elif choice == "6":
                # View Members
                print("\n--- View Members ---")
                members = service.view_members()
                
                if not members:
                    print("\n👥 No members found.")
                else:
                    print(f"\n👥 Members ({len(members)} total):")
                    print("-" * 60)
                    for member in members:
                        print(f"   {member}")
                    print("-" * 60)
            
            elif choice == "7":
                # View Loans
                print("\n--- View Loans ---")
                loans = service.view_loans()
                
                if not loans:
                    print("\n📭 No loans found.")
                else:
                    print(f"\n📋 Loans ({len(loans)} total):")
                    print("-" * 60)
                    for loan in loans:
                        print(f"   {loan}")
                    print("-" * 60)
            
            elif choice == "8":
                # Exit
                print("\n--- Exit Program ---")
                print("\n👋 Thank you for using Library Management System!")
                print("Program closed.\n")
                break
            
            else:
                print("\n❌ Invalid choice. Please enter a number between 1 and 8.")
        
        except Exception as e:
            print(f"\n❌ Unexpected error: {e}")

if __name__ == "__main__":
    main()
