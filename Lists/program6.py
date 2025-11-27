n = int(input("Enter nums: "))
lst = []

for i in range(n):
    num = int(input("Enter number: "))  
    if num % 2 == 0:                      
        lst.append(num)

print("Even numbers:",lst)