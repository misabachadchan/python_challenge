class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self):
        amount = int(input("Enter deposit amount: "))  # INPUT INSIDE METHOD
        self.balance += amount

    def display(self):
        print("Balance:", self.balance)

# Usage
account = BankAccount(5000)
account.deposit()   # asks user for input here
account.display()
