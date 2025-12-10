from functools import reduce

nums = list(map(int, input("Enter numbers: ").split()))
div3 = list(filter(lambda x: x % 3 == 0, nums))

if div3:
    result = reduce(lambda x, y: x if x > y else y, div3)
    print("Largest divisible by 3:", result)
else:
    print("No number divisible by 3 found")
