
---

# 📘Day-8 Python Dictionary

## ## **1. What is a Dictionary?**

A **dictionary** in Python is a collection of **key–value pairs**.

* Keys must be **unique**
* Keys must be **immutable** (string, number, tuple)
* Values can be **anything**
* Dictionary is **mutable**

### ✔ Example:

```python
student = {
    "name": "Misaba",
    "age": 21,
    "branch": "CSE"
}
```

---

# ## **2. Creating a Dictionary**

```python
d = {}
d = {"a": 1, "b": 2}
d = dict(name="misaba", age=21)
```

---

# ## **3. Accessing Values**

```python
print(student["name"])      # direct access
print(student.get("usn"))   # returns None if key missing
print(student.get("city", "Not available"))  # default value
```

---

# ## **4. Adding / Updating Items**

```python
student["email"] = "abc@gmail.com"
student.update({"city": "Vijayapura", "year": 2025})
```

---

# ## **5. Deleting Items**

```python
del student["age"]          # delete key
student.pop("branch")       # delete & return value
student.popitem()           # removes last inserted item
student.clear()             # empty dictionary
```

---

# ## **6. Looping Through a Dictionary**

### ✔ Keys only

```python
for key in student:
    print(key)
```

### ✔ Values only

```python
for value in student.values():
    print(value)
```

### ✔ Keys + Values

```python
for key, value in student.items():
    print(key, ":", value)
```

---

# ## **7. Dictionary Methods (Important)**

| Method       | Description              |
| ------------ | ------------------------ |
| get()        | Returns value or default |
| keys()       | Returns all keys         |
| values()     | Returns all values       |
| items()      | Returns key–value pairs  |
| update()     | Adds or updates          |
| pop()        | Removes by key           |
| popitem()    | Removes last inserted    |
| clear()      | Empties dictionary       |
| setdefault() | Insert if key missing    |
| copy()       | Shallow copy             |

---

# ## **8. Useful Programs**

### ✔ Count character frequency

```python
string = "banana"
d = {}

for ch in string:
    d[ch] = d.get(ch, 0) + 1

print(d)
```

---

### ✔ Count word frequency

```python
words = input("Enter text: ").split()
d = {}

for w in words:
    d[w] = d.get(w, 0) + 1

print(d)
```

---

### ✔ Find key with maximum value

```python
max_key = max(d, key=d.get)
print(max_key)
```

---

### ✔ Find key with minimum value

```python
min_key = min(d, key=d.get)
print(min_key)
```

---

### ✔ Sort dictionary by keys

```python
sorted_by_keys = dict(sorted(d.items()))
print(sorted_by_keys)
```

---

### ✔ Sort dictionary by values

```python
sorted_by_values = dict(sorted(d.items(), key=lambda x: x[1]))
print(sorted_by_values)
```

---

# ## **9. Merging Dictionaries**

### ✔ Using update()

```python
d1 = {"a": 1}
d2 = {"b": 2}
d1.update(d2)
```

### ✔ Using unpacking

```python
merged = {**d1, **d2}
```

---

# ## **10. Dictionary Comprehension**

```python
square = {x: x*x for x in range(1,6)}
print(square)
```

---

# 📘 Python Dictionary practice Questions

## 1. Create a dictionary of 5 key-value pairs and print it.

## 2. Access value by key.

## 3. Add a new key-value pair.

## 4. Update value of an existing key.

## 5. Delete a key-value pair using `del`.

## 6. Delete a key-value pair using `.pop()`.

## 7. Get all keys using `.keys()`.

## 8. Get all values using `.values()`.

## 9. Get all items (key-value pairs) using `.items()`.

## 10. Check if a key exists in a dictionary.

## 11. Check if a value exists in a dictionary.

## 12. Find the length of a dictionary.

## 13. Merge two dictionaries.

## 14. Clear a dictionary.

## 15. Copy a dictionary.

## 16. Count the frequency of characters in a string using a dictionary.

## 17. Count the frequency of words in a sentence.

## 18. Find the key with maximum value.

## 19. Find the key with minimum value.

## 20. Sort dictionary by keys.

## 21. Sort dictionary by values.

