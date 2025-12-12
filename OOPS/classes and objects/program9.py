class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self):
        amount = int(input("Enter deposit amount: "))  # INPUT INSIDE METHOD
        self.balance += amount

    def withdraw(self):
        amount=int(input("Enter amount to withdraw:"))
        if amount<=self.balance:
             self.balance-=amount
        else:
            print("Insufficient balance")


    def display(self):
        print("Balance:", self.balance)
        print

    

# Usage
account = BankAccount(5000)
account.deposit()   # asks user for input here
account.withdraw()
account.display()
