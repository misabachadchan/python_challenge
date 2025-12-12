class Student():
    def __init__(self,name):
        self.name=name
        self.marks=[]

    def mark(self):
        for i in range(6):
            m = float(input(f"Enter mark {i+1}: "))
            self.marks.append(m)

    def percentage(self):
        return (sum(self.marks)/600)*100

    def display(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")
        print("Percentage:",self.percentage())


name = input("Enter name: ")
s1 = Student(name)

s1.mark()
s1.percentage()
s1.display()
    

    

