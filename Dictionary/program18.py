d = {'a': 10, 'b': 5, 'c': 20}

max_key = max(d, key=d.get)
print("Key with maximum value:", max_key)
