list1 = list(map(int, input("Enter elements of list1: ").split()))
list2 = list(map(int, input("Enter elements of list2: ").split()))

common = set(list1) & set(list2)   # intersection
print("Common elements:", common)
print("Count of common elements:", len(common))
