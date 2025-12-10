# 8. Check if a string is palindrome
is_palindrome = lambda s: s == s[::-1]
s = input("Enter a string: ")
print("Is palindrome?", is_palindrome(s))
