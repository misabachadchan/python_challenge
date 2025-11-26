def sum_natural(n):
    return sum(range(1, n+1))

x = int(input("Enter N: "))
print("Sum of first N natural numbers:", sum_natural(x))
