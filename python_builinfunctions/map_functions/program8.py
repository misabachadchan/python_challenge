celsius = list(map(int, input("Enter temperatures: ").split()))
result = list(map(lambda c: (c*9/5)+32, celsius))
print(result)
