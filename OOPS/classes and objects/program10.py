class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def Bonus(self):
        return self.salary+(self.salary*0.1)
    
    def display(self):
        print("Name:",self.name)
        print("Salary:",self.salary)
        print("Bonused salary:",self.Bonus())

a=input("Enter name:")
b=int(input("Enter salary:"))

show=Employee(a,b)
show.display()