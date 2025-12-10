words = input("Enter words: ").split()
result = list(filter(lambda x: x.isupper(), words))
print(result)
