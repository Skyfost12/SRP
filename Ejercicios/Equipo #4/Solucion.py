class Book:

    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies


class User:

    def __init__(self, name, id, email):
        self.name = name
        self.id = id
        self.email = email


class Loan:

    def __init__(self):
        self.loans = []

    def loan_book(self, user, book):
        if book.copies > 0:
            book.copies -= 1
            self.loans.append(
                {"user_id": user.id, "book_title": book.title})
            return True
        return False

    def return_book(self, user, book):
        for loan in self.loans:
            if loan["user_id"] == user.id and loan["book_title"] == book.title:
                self.loans.remove(loan)
                book.copies += 1
                return True
        return False


class Library:

    def __init__(self) -> None:
        self.books = []
        self.users = []
        self.loans_service = Loan()

    def add_book(self, book):
        self.books.append(book)

    def add_user(self, user):
        self.users.append(user)

    def loan_book(self, user_id, book_title):
        user = next((u for u in self.users if u.id == user_id), None)
        book = next((b for b in self.books if b.title == book_title), None)
        if user and book:
            return self.loans_service.loan_book(user, book)
        return False

    def return_book(self, user_id, book_title):
        user = next((u for u in self.users if u.id == user_id), None)
        book = next((b for b in self.books if b.title == book_title), None)
        if user and book:
            return self.loans_service.return_book(user, book)
        return False