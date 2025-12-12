class BankAccount():
    def __init__(self,balance):
        self.balance=balance

    def display(self):
        print(f"Balance is {self.balance}")

a=BankAccount(5000)
a.display()
