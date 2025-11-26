def count_consonants(s):
    count = 0
    for ch in s:
        if ch.isalpha() and ch.lower() not in "aeiou":
            count += 1
    return count

s = input("Enter string: ")
print("Number of consonants:", count_consonants(s))
