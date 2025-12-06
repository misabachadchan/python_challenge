tup=tuple(map(int,input("Enter numbers:").split()))
n=int(input("Enter the number to check occureneces:"))
num=tup.count(n)

print(f"{n} occurs {num} times")

