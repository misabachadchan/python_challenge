target = input("Enter word to count: ").lower()

with open("hello.txt", "r") as f:
    text = f.read().lower()

count = text.split().count(target)
print("Occurrences:", count)
