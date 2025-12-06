list1 = list(map(int, input("Enter elements of list1: ").split()))
list2 = list(map(int, input("Enter elements of list2: ").split()))

intersection = set(list1).intersection(set(list2))
print("Elements in both lists:", intersection)
