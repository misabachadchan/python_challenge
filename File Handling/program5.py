with open("example.txt", "r") as f:
    text = f.read()
    words = text.split()
    print("Number of words:", len(words))
