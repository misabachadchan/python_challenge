# 4. Maximum of two numbers
maximum = lambda x, y: x if x > y else y
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Maximum:", maximum(a, b))
