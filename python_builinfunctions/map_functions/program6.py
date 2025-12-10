list1 = list(map(int, input("Enter list1: ").split()))
list2 = list(map(int, input("Enter list2: ").split()))
result = list(map(lambda x, y: x*y, list1, list2))
print(result)
