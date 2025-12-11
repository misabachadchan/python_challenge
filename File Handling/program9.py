word = input("Enter word to search: ")

with open("hello.txt", "r") as f:
    for line in f:
        if word in line:
            print(line.strip())
