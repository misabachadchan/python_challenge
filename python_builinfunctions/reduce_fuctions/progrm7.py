from functools import reduce

nums = list(map(int, input("Enter numbers: ").split()))
result = reduce(lambda x, y: x + y*y, nums, 0)
print("Sum of squares:", result)
