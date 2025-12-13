class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        self.history=[]

    def deposit(self):
        amount = int(input("Enter deposit amount: "))  # INPUT INSIDE METHOD
        self.balance += amount
        self.history.append(f"Deposited: {amount}")

    def withdraw(self):
        amount = int(input("Enter amount to withdraw: "))
        if amount <= self.balance:
            self.balance -= amount
            self.history.append(f"Withdrawn: {amount}")
        else:
            self.history.append("Failed withdrawal (Insufficient balance)")
            print("Insufficient balance")

    def transaction_history(self):
        print("Current Balance:", self.balance)
        print("Transaction History:")
        for t in self.history:
            print("-", t)


# Usage
account = BankAccount(5000)
account.deposit()
account.withdraw()
account.transaction_history()