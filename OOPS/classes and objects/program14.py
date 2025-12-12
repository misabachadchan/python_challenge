class BookStore():
    def  __init__(self):
        self.books=[]

    def Add_Books(self):
        n=int(input("Enter number to add:"))
        for i in range(n):
            m=input(f"Enter book {i+1}:")
            self.books.append(m)

    def display(self):
        print("Books in store:")
        for i, b in enumerate(self.books, start=1):
            print(i, b)
        
       
        
book=BookStore()
book.Add_Books()
book.display()
            
            
            



