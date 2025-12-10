nums = list(map(int, input("Enter numbers: ").split()))
result = list(filter(lambda x: x > 0, nums))
print(result)
