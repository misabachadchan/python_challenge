from functools import reduce

words = input("Enter words: ").split()
result = reduce(lambda x, y: x + y, words)
print("Concatenated string:", result)
