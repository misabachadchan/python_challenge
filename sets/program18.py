list1 = list(map(int, input("Enter elements of list1: ").split()))
list2 = list(map(int, input("Enter elements of list2: ").split()))

diff = set(list1).difference(set(list2))
print("Elements in list1 not in list2:", diff)
