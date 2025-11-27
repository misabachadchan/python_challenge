def add(a,b):
    return a+b
    
def sub(a,b):
    return a-b
    
def multiply(a,b):
    return a*b

def divide(a,b):
    if(b!=0):
        return a/b
    else:
        print("Can't divide by zero ")


print("1.Addition")
print("2.Substraction")
print("3.Multipliaction")
print("4.Division")

n=int(input("Enter number :"))
x=int(input("Enter number 1:"))
y=int(input("Enter number 2:"))

if(n==1):
    print("Sum:",add(x,y))
elif(n==2):
    print("Substract:",sub(x,y))
elif(n==3):
    print("Multiply:",multiply(x,y))
elif(n==4):
    print("Division:",divide(x,y))
else:
    print("Not a valid number")
