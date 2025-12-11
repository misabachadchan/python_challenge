numbers = [10, 20, 30, 40, 50]

with open("numbers.txt", "w") as f:
    for num in numbers:
        f.write(str(num) + "\n")
