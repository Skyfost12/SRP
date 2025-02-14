using System;
using System.Collections.Generic;

class Library
{
    private List<string[]> books;
    private List<string[]> users;
    private List<string[]> loans;

    public Library()
    {
        books = new List<string[]>();
        users = new List<string[]>();
        loans = new List<string[]>();
    }

    public void AddBook(string title, string author, int copies)
    {
        books.Add(new string[] { title, author, copies.ToString() });
    }

    public void AddUser(string name, string id, string email)
    {
        users.Add(new string[] { name, id, email });
    }

    public bool LoanBook(string userId, string bookTitle)
    {
        foreach (var book in books)
        {
            if (book[0] == bookTitle && int.Parse(book[2]) > 0)
            {
                book[2] = (int.Parse(book[2]) - 1).ToString();
                loans.Add(new string[] { userId, bookTitle });
                return true;
            }
        }
        return false;
    }

    public bool ReturnBook(string userId, string bookTitle)
    {
        for (int i = 0; i < loans.Count; i++)
        {
            if (loans[i][0] == userId && loans[i][1] == bookTitle)
            {
                loans.RemoveAt(i);
                foreach (var book in books)
                {
                    if (book[0] == bookTitle)
                    {
                        book[2] = (int.Parse(book[2]) + 1).ToString();
                        return true;
                    }
                }
            }
        }
        return false;
    }
}
