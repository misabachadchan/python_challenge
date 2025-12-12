import math

class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def DistanceFromOrigin(self):
        return math.sqrt(self.x**2+ self.y**2)
    
    def show(self):
        print("Distance From Origin :",self.DistanceFromOrigin())
    
point1=int(input("Enter X:"))
point2=int(input("Enter Y:"))

coordinate=Point(point1,point2)
coordinate.DistanceFromOrigin()
coordinate.show()
