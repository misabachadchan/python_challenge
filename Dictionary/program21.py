d = {'c': 3, 'a': 1, 'b': 2}

sorted_by_values = dict(sorted(d.items(), key=lambda x: x[1]))
print(sorted_by_values)
