# 10. Check if a number is divisible by 5
div_by_5 = lambda x: x % 5 == 0
n = int(input("Enter a number: "))
print("Divisible by 5?", div_by_5(n))
