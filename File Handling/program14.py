with open("multi.txt", "w") as f:
    while True:
        data = input("Enter text (or 'stop' to end): ")
        if data.lower() == "stop":
            break
        f.write(data + "\n")
