from functools import reduce

nums = list(map(int, input("Enter numbers: ").split()))
even_nums = list(filter(lambda x: x % 2 == 0, nums))

if even_nums:
    result = reduce(lambda x, y: x * y, even_nums)
    print("Product of even numbers:", result)
else:
    print("No even numbers found")
