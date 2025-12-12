class Temperature:
    def __init__(self,celcius,farenheit):
        self.celcius=celcius
        self.farenheit=farenheit

    def CelciusToFareheit(self):
        return (self.celcius*1.8)+32
    
    def FareheitToCelcius(self):
        return (self.farenheit-32)/1.8
    
    def display(self):
        print("Celcius To Fareheit:",self.CelciusToFareheit())
        print(" Fareheit To Celcius :",self.FareheitToCelcius())

cel=float(input("Enter Celicus:"))
faren=float(input("Enter Farenheit:"))

temp=Temperature(cel,faren)
temp.display()
    