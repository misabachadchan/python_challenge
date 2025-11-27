n = list(map(int, input("Enter numbers: ").split()))
k = int(input("Enter rotation : "))

k = k % len(n)  # to avoid overflow
rotated = n[-k:] + n[:-k]

# rotation by right k rotated = n[k:] + n[:k]

print(rotated)