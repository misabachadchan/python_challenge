n=input("Enter String:")
count=0
for i in n:
    if(i.islower()):
        count+=1
print("total Lowercase letters:",count)