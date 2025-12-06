tup=tuple(map(int,input("Enter marks:").split()))
if len(tup) > 0:
    average = sum(tup) / len(tup)
    print("Average:", average)
else:
    print("No marks entered")

