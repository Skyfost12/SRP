class Library:
    def __init__(self) -> None:
        self.books = []
        self.users = []
        self.loans = []

    def add_book(self, title, author, copies):
        self.books.append({"title": title, "author": author, "copies": copies})

    def add_user(self, name, id, email):
        self.users.append({"name": name, "id": id, "email": email})

    def loan_book(self, user_id, book_title):
        for book in self.books:
            if book["title"] == book_title and book["copies"] > 0:
                book["copies"] -= 1
                self.loans.append(
                    {"user_id": user_id, "book_title": book_title})
                return True
        return False

    def return_book(self, user_id, book_title):
        for loan in self.loans:
            if loan["user_id"] == user_id and loan["book_title"] == book_title:
                self.loans.remove(loan)
                for book in self.books:
                    if book["title"] == book_title:
                        book["copies"] += 1
                    return True
        return False