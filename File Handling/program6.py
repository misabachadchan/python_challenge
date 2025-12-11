with open("example.txt", "r") as src, open("hello.txt", "w") as dest:
    dest.write(src.read())
