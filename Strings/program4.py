string = input("Enter the string: ")
count = 0
vowels = ['a', 'e', 'i', 'o', 'u']

for ch in string.lower():
    if ch.isalpha() and ch not in vowels:
        count += 1

print("Consonants:", count)
