n=input("Enter String:")
count=0
for i in n:
    if(i.isupper()):
        count+=1
print("total uppercase letters:",count)