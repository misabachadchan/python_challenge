n=int(input("Enter number"))
sum=0
for i in range(n):
    num=int(input("Enter the numbers:"))
    if num%2==0:
        sum+=num
print(sum)