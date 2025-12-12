class Rectangle():
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length* self.width
    
# result=rectangle(15,10)
# print("Area is:",result.area())
    # Taking input from user
l = float(input("Enter length: "))
w = float(input("Enter width: "))

# Create object
r = Rectangle(l, w)

# Print area
print("Area:", r.area())
