

---

# Day-10 📘 Python Sets

Sets are **unordered collections of unique elements** in Python.
They are commonly used for membership testing, removing duplicates, and performing mathematical set operations.

---

## 📌 What is a Set?

A **set** in Python is defined using **curly braces `{}`** or the `set()` constructor.

```python
s1 = {1, 2, 3, 4, 5}
s2 = set([1, 2, 3])
s3 = set()  # empty set
```

✅ Sets **do not allow duplicates** and **do not maintain order**.

---

## 📌 Set Characteristics

| Feature           | Description                                     |
| ----------------- | ----------------------------------------------- |
| Unordered         | Elements have no index                          |
| Mutable           | You can add or remove elements                  |
| Unique Elements   | Duplicates are automatically removed            |
| Iterable          | Can loop through each element                   |
| Supports Math Ops | Union, Intersection, Difference, Symmetric Diff |

---

## 📌 Creating Sets

```python
s = {1, 2, 3, 4, 5}          # set with numbers
s_str = {"apple", "banana"}   # set with strings
empty = set()                 # empty set
```

⚠️ `{}` creates an empty dictionary, not a set. Use `set()` for empty sets.

---

## 📌 Sets Methods 

| Method       | Description                           | Example         | Output          |
| ------------ | ------------------------------------- | --------------- | --------------- |
| `.add()`     | Adds element to set                   | `s.add(6)`      | `{1,2,3,4,5,6}` |
| `.remove()`  | Removes element, error if not present | `s.remove(3)`   | `{1,2,4,5}`     |
| `.discard()` | Removes element, no error if absent   | `s.discard(10)` | `{1,2,4,5}`     |
| `.pop()`     | Removes arbitrary element             | `s.pop()`       | Element removed |
| `.clear()`   | Removes all elements                  | `s.clear()`     | `set()`         |
| `.copy()`    | Returns shallow copy of set           | `s2 = s.copy()` | `{1,2,4,5}`     |

---

## 📌 Set Operations 

| Operation            | Method / Operator               | Example             | Output               |     |               |
| -------------------- | ------------------------------- | ------------------- | -------------------- | --- | ------------- |
| Union                | `.union()` / `                  | `                   | `s1.union(s2)` / `s1 | s2` | `{1,2,3,4,5}` |
| Intersection         | `.intersection()` / `&`         | `s1 & s2`           | `{2,3}`              |     |               |
| Difference           | `.difference()` / `-`           | `s1 - s2`           | `{1,4,5}`            |     |               |
| Symmetric Difference | `.symmetric_difference()` / `^` | `s1 ^ s2`           | `{1,4,5}`            |     |               |
| Subset               | `.issubset()`                   | `s2.issubset(s1)`   | True/False           |     |               |
| Superset             | `.issuperset()`                 | `s1.issuperset(s2)` | True/False           |     |               |
| Membership           | `in` / `not in`                 | `2 in s1`           | True                 |     |               |
| Length               | `len(s)`                        | `len(s1)`           | 5                    |     |               |
| Convert list to set  | `set(list)`                     | `set([1,2,2,3])`    | `{1,2,3}`            |     |               |

---

## 📌 Converting Lists to Sets

```python
lst = [1, 2, 2, 3, 4, 4]
unique = set(lst)   # {1,2,3,4}
```

✅ Useful for removing duplicates or finding common/unique elements.

---

## 📌 Iterating Through a Set

```python
s = {1, 2, 3}
for elem in s:
    print(elem)
```

---

## 📌 When to Use Sets?

* Remove duplicates from a list
* Membership testing (`in`, `not in`)
* Mathematical operations like union, intersection, difference
* Fast lookup (average O(1) time)

---

# 📝 Set Practice Problems 

## 1. Create a set with 5 numbers and print it

## 2. Add an element to a set

## 3. Remove an element from a set

## 4. Check if an element exists in a set

## 5. Find the length of a set

## 6. Create a set from a list (remove duplicates)

## 7. Clear a set

## 8. Union of two sets

## 9. Intersection of two sets

## 10. Difference between two sets

## 11. Symmetric difference between two sets

## 12. Check if one set is subset of another

## 13. Check if one set is superset of another

## 14. Copy a set

## 15. Find unique characters in a string using set

## 16. Remove duplicates from a list using set

## 17. Count common elements between two lists using sets

## 18. Find elements in list1 not in list2 using sets

## 19. Check if a list has duplicates using sets

## 20. Find all elements that appear in both lists (intersection)


