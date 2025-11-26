def first_natural(n):
    return [i for i in range(1, n+1)]

x = int(input("Enter N: "))
print("First N natural numbers:", first_natural(x))
