words = input("Enter words (with spaces): ").split(" ")
result = list(filter(lambda x: x != "", words))
print(result)
