nums = list(map(int, input("Enter numbers: ").split()))
result = list(filter(lambda x: x > 10, nums))
print(result)
