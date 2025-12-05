import datetime

class Book:
    def __init__(self, book_id, title, author, quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.quantity = quantity

class Member:
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email

class LibrarySystem:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added successfully.")

    def register_member(self, member):
        self.members.append(member)
        print(f"Member '{member.name}' registered.")

    def issue_book(self, book_id, member_id):
        # Logic to issue book
        print(f"Book {book_id} issued to {member_id} on {datetime.date.today()}")

# Main execution
if __name__ == "__main__":
    lib = LibrarySystem()
    lib.add_book(Book(1, "The Great Gatsby", "F. Scott Fitzgerald", 5))
    lib.register_member(Member(101, "Student One", "student@example.com"))
    lib.issue_book(1, 101)
