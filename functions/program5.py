def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

x = int(input("Enter numerator: "))
y = int(input("Enter denominator: "))
print("Division:", divide(x, y))
