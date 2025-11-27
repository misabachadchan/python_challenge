n = list(map(int, input("Enter numbers: ").split()))

largest = second = float('-inf')

for x in n:
    if x > largest:
        second = largest
        largest = x
    elif x > second and x != largest:
        second = x

print("Second largest:",second)