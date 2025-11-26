def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

x = int(input("Enter number 1: "))
y = int(input("Enter number 2: "))
print("LCM:", lcm(x, y))