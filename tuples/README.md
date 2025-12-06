
# Day-9 📘 Python Tuples

Tuples are one of the built-in data types in Python used to store multiple values in a **single variable**.
They are **ordered** and **immutable** collections.

---

## 📌 What is a Tuple?

A **tuple** in Python is a collection of items enclosed in **parentheses `()`** and separated by commas.

```python
t1 = (10, 20, 30)
t2 = ("apple", "banana", "mango")
t3 = (1, "Python", 3.5, True)
```

✅ Tuples can store **mixed data types**

---

## 📌 Tuple Characteristics

| Feature           | Description                              |
| ----------------- | ---------------------------------------- |
| Ordered           | Elements have fixed positions (indexing) |
| Immutable         | Cannot modify elements after creation    |
| Allows duplicates | Same value can appear multiple times     |
| Iterable          | Can loop through items                   |
| Faster than list  | Better performance than lists            |

---

## 📌 Creating Tuples

```python
t = (1, 2, 3)
single = (10,)        # single-element tuple
empty = ()
```

⚠️ Without a comma, `(10)` is **not** a tuple.

---

## 📌 Tuple Indexing

```
t = ("P", "Y", "T", "H", "O", "N")

Index:        0  1  2  3  4  5
Negative:    -6 -5 -4 -3 -2 -1
```

```python
print(t[0])    # P
print(t[-1])   # N
```

---

## 📌 Tuple Slicing

```python
t = (10, 20, 30, 40, 50)

print(t[1:4])   # (20, 30, 40)
print(t[:3])    # (10, 20, 30)
print(t[::2])   # (10, 30, 50)
```

---

## 📌 Tuple Operations

| Operation     | Example         | Output      |
| ------------- | --------------- | ----------- |
| Concatenation | `(1,2) + (3,4)` | `(1,2,3,4)` |
| Repetition    | `(1,2) * 2`     | `(1,2,1,2)` |
| Membership    | `2 in (1,2,3)`  | True        |
| Length        | `len((1,2,3))`  | 3           |

---

## 📌 Tuple Methods (Built-in)

| Method    | Description                     | Example                |
| --------- | ------------------------------- | ---------------------- |
| `count()` | Count occurrences of an element | `(1,2,2).count(2)`     |
| `index()` | Find index of an element        | `(10,20,30).index(20)` |

📝 Tuples have **only two methods** because they are immutable.

---

## 📌 Packing & Unpacking Tuples

### Packing

```python
t = 10, 20, 30
```

### Unpacking

```python
a, b, c = t
```

---

## 📌 Nested Tuples

```python
t = ((1, 2), (3, 4), (5, 6))
print(t[1][0])   # 3
```

---

## 📌 Converting Between List & Tuple

```python
lst = [1, 2, 3]
t = tuple(lst)

t2 = (4, 5, 6)
lst2 = list(t2)
```

# 📝 Tuple Practice Problems – Python

## 1. Create a tuple with 5 numbers and print it

## 2. Access the first and last elements of a tuple

## 3. Find the length of a tuple

## 4. Concatenate two tuples

## 5. Repeat a tuple multiple times

## 6. Check if an element exists in a tuple

## 7. Slice a tuple to get a sub-tuple

## 8. Find the index of an element in a tuple

## 9. Count occurrences of an element in a tuple

## 10. Convert a list to a tuple

## 11. Convert a tuple to a list

## 12. Unpack a tuple into variables

## 13. Swap two tuples

## 14. Find the largest and smallest element in a tuple

## 15. Take input from user, store as a tuple, print reversed tuple

## 16. Merge multiple tuples into one

## 17. Create a tuple of tuples and access elements

## 18. Tuple of student marks: calculate average

## 19. Create a tuple with mixed data types and print only numbers



