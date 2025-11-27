#First method using max function

n=list(map(int,input("Enter numbers:").split()))
print(n)
print("minimun number is:",min(n))

#Second method using Loops

n=list(map(int,input("Enter numbers:").split()))
smallest=n[0]
for x in n:
    if smallest>x:
        smallest=x

print("minimun number is:",smallest)



