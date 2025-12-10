# 7. Absolute value of a number
absolute = lambda x: x if x >= 0 else -x
n = int(input("Enter a number: "))
print("Absolute value:", absolute(n))
