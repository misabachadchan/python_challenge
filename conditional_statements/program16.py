a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
if a>b:
    if(a>c):
        large=a
    else:
        large=c
else:
    if(b>c):
        large=b
    else:
        large=c
print(large,"is largest number")