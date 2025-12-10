from functools import reduce

nums = list(map(int, input("Enter numbers: ").split()))
result = reduce(lambda x, y: x if x < y else y, nums)
print("Minimum:", result)
