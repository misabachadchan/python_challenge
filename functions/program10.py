def even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

x = int(input("Enter number: "))
print(even_odd(x))
