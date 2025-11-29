string=input("enter string:").split()
d={}
for word in string:
    if word in d:
        d[word]+=1
    else:
        d[word]=1
print(d)

    
