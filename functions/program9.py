def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

x = int(input("Enter number: "))
print("Factorial:", factorial(x))
