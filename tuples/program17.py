
t1 = tuple(map(int, input("Enter elements of tuple 1: ").split()))
t2 = tuple(map(int, input("Enter elements of tuple 2: ").split()))
t3 = tuple(map(int, input("Enter elements of tuple 3: ").split()))

#it works a matrix
tup = (t1, t2, t3)

print("Tuple of tuples:", tup)
print("First tuple:", tup[0])
print("Element from second tuple:", tup[1][0])
