class Library {
    constructor() {
        this.books = [];
        this.users = [];
        this.loans = [];
    }

    addBook(title, author, copies) {
        this.books.push([title, author, copies]);
    }

    addUser(name, id, email) {
        this.users.push([name, id, email]);
    }

    loanBook(userId, bookTitle) {
        for (let book of this.books) {
            if (book[0] === bookTitle && book[2] > 0) {
                book[2] -= 1;
                this.loans.push([userId, bookTitle]);
                return true;
            }
        }
        return false;
    }

    returnBook(userId, bookTitle) {
        for (let i = 0; i < this.loans.length; i++) {
            if (this.loans[i][0] === userId && this.loans[i][1] === bookTitle) {
                this.loans.splice(i, 1);
                for (let book of this.books) {
                    if (book[0] === bookTitle) {
                        book[2] += 1;
                        return true;
                    }
                }
            }
        }
        return false;
    }
}
