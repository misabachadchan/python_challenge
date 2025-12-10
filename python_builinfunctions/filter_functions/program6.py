nums = list(map(int, input("Enter numbers: ").split()))
result = list(filter(lambda x: x % 3 == 0, nums))
print(result)
