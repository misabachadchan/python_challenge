from math import pi
class Circle():
    def __init__(self,radius):
        self.radius=radius

    def Circumference(self):
        return 2*pi*self.radius
    
    def display(self):
        print("Circumference of circle is:",self.Circumference())

r=float(input("Enter radius:"))
circle=Circle(r)
circle.Circumference()
circle.display()




