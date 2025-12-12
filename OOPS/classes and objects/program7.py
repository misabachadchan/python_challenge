class Book():
    def __init__(self,title,author):
        self.title=title
        self.author=author

    def display(self):
        print("Title of Book:",self.title)
        print("Author of Book:",self.author)

a=input("Enter title:")
b=input("Enter author:")

show=Book(a,b)
show.display()
