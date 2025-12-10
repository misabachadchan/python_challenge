s = input("Enter string: ")
vowels = "aeiouAEIOU"
result = "".join(filter(lambda x: x not in vowels, s))
print(result)
