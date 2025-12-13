class Car:
    def __init__(self, brand, fuel):
        self.brand = brand
        self.fuel = fuel

    def drive(self):
        if self.fuel > 0:
            self.fuel -= 1
            print("Car is driving")
        else:
            print("No fuel to drive")

    def refuel(self):
        amount = int(input("Enter fuel amount to add: "))
        self.fuel += amount
        print("Car refueled")

    def display(self):
        print("Brand:", self.brand)
        print("Fuel:", self.fuel)


brand = input("Enter car brand: ")
fuel = int(input("Enter initial fuel: "))

car = Car(brand, fuel)
car.drive()
car.refuel()
car.display()
