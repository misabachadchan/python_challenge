total = 0

with open("numbers.txt", "r") as f:
    for line in f:
        total += int(line.strip())

print("Sum:", total)
