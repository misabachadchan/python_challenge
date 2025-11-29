d = {'a': 10, 'b': 5, 'c': 20}

min_key = min(d, key=d.get)
print("Key with minimum value:", min_key)
