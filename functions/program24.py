def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

x = int(input("Enter number 1: "))
y = int(input("Enter number 2: "))
print("GCD:", gcd(x, y))
