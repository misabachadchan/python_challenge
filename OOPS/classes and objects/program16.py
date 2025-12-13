class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def is_above_average(self, average_salary):
        if self.salary > average_salary:
            print("Salary is above average")
        else:
            print("Salary is not above average")


# Usage
name = input("Enter name: ")
salary = int(input("Enter salary: "))
avg_salary = int(input("Enter average salary: "))

emp = Employee(name, salary)
emp.is_above_average(avg_salary)
