from functools import reduce

n = int(input("Enter a number: "))
nums = list(range(1, n + 1))
result = reduce(lambda x, y: x * y, nums)
print("Factorial:", result)
