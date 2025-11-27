#First method using max function

n=list(map(int,input("Enter numbers:").split()))
print(n)
print("maxium number is:",max(n))

#Second method using Loops

n=list(map(int,input("Enter numbers:").split()))
largest=n[0]
for x in n:
    if largest<x:
        largest=x

print("maxium number is:",largest)



