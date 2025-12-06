tup=tuple(map(int,input("Enter numbers:").split()))
n=int(input("Enter num to check wheter exist or not:"))
if n in tup:
    print(n,"exist")
else:
    print(n,"not exist")
