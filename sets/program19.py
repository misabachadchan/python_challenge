lst = list(map(int, input("Enter elements of list: ").split()))

if len(lst) != len(set(lst)):
    print("List has duplicates")
else:
    print("List has no duplicates")
