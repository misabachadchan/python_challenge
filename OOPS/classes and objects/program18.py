class Library():
    def __init__(self):
        self.books=[]

    def add_books(self):
        n=int(input("Enter number of books to add:"))
        for i in range(n):
            book=input(f"Enter book name {i+1}:").lower()
            self.books.append(book)

    def Remove_book(self):
        book=input("Enter book name to remove:").lower()
        if book in self.books:
            self.books.remove(book)
            print("Book removed successfully")
        else:
            print("Book not found")

        



    def show(self):
        print("Books:",self.books)


lib=Library()
lib.add_books()
lib.Remove_book()
lib.show()
