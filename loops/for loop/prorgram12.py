n=int(input("Enter how many series:"))
a,b=0,1
total=0
for i in range(n):
    print(a,end=" ")
    total+=a
    a,b=b,a+b
print("Sum of fibonacci series is:",total)