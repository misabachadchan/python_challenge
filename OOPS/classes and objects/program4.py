class Circle():
    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        return 3.14*self.radius*self.radius
    
r=int(input("Enter radius:"))

result=Circle(r)
print("Area of circle is:",result.area())