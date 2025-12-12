class Student():
    def __init__(self,name):
        self.name=name
        self.marks=[]

    def mark(self):
        for i in range(6):
            m = float(input(f"Enter mark {i+1}: "))
            self.marks.append(m)

    def display(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")


name = input("Enter name: ")
s1 = Student(name)

s1.mark()
s1.display()
    

    

