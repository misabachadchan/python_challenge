words = input("Enter words: ").split()
result = list(filter(lambda x: len(x) > 4, words))
print(result)
