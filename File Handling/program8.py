data = input("Enter text: ")

with open("usertext.txt", "w") as f:
    f.write(data)
