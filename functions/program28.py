def swap(a, b):
    return b, a

x = int(input("Enter number 1: "))
y = int(input("Enter number 2: "))
x, y = swap(x, y)
print("After swapping: x =", x, ", y =", y)
