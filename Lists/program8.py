#first method
n=list(map(int,input("Enter number:").split()))
new=set(n)
print(new)

#Second method
n=list(map(int,input("Enter numbers:").split()))
lst=[]
for x in n:
    if x not in lst:
        lst.append(x)
print(lst)
