# Day-6 Python Lists

## 1. What is a List?

A **list** in Python is an ordered, changeable (mutable), and indexed collection of items.
Lists can store **different data types** (int, float, string, list, etc.).

**Example:**

```python
numbers = [10, 20, 30]
mixed = [10, "hello", 3.5]
```

---

## 2. Basic List Operations

### **Create a List**

```python
lst = [1, 2, 3, 4]
```

### **Access Elements**

```python
lst[0]   # first element
lst[-1]  # last element
```

### **Modify Elements**

```python
lst[1] = 10
```

### **Length of List**

```python
len(lst)
```

### **Append Element**

```python
lst.append(50)
```

### **Insert at Position**

```python
lst.insert(2, 100)
```

### **Remove Element**

```python
lst.remove(20)
```

### **Delete by Index**

```python
del lst[1]
```

### **Pop an Element**

```python
lst.pop()      # removes last
lst.pop(2)     # removes index 2
```

### **Check if Element Exists**

```python
if 10 in lst:
    print("Present")
```

---

## 3. List Slicing

```python
lst[1:5]
lst[:3]
lst[2:]
lst[::-1]  # reverse list
```

---

## 4. List Methods Summary

| Method      | Description             |
| ----------- | ----------------------- |
| `append()`  | Add item to end         |
| `insert()`  | Insert at index         |
| `remove()`  | Remove first occurrence |
| `pop()`     | Remove element by index |
| `clear()`   | Empty list              |
| `sort()`    | Sort list               |
| `reverse()` | Reverse list            |
| `count()`   | Count occurrences       |
| `extend()`  | Add multiple elements   |

---

## 5. Iterating Through a List

### **Using for loop**

```python
for x in lst:
    print(x)
```

### **Using while loop**

```python
i = 0
while i < len(lst):
    print(lst[i])
    i += 1
```

---

## 6. List Comprehensions

Short syntax for creating lists:

```python
squares = [x*x for x in range(1, 11)]
evens = [x for x in lst if x % 2 == 0]
```

---

## 7. Nested Lists

```python
matrix = [[1, 2], [3, 4]]
print(matrix[0][1])
```

---

# 📌 List Practice Questions

### **1. Find the largest element in a list.**

### **2. Find the smallest element in a list.**

### **3. Sum all elements in a list.**

### **4. Count occurrences of an element in a list.**

### **5. Reverse a list.**

### **6. Print all even numbers from a list.**

### **7. Print all odd numbers from a list.**

### **8. Remove duplicates from a list.**

### **9. Find the second largest number in a list.**

### **10. Find the sum of all odd numbers in a list.**

### **11. Find the sum of all even numbers in a list.**

### **12. Check if a list is sorted in ascending order.**

### **13. Merge two lists alternately.**

### **14. Rotate a list by K positions.**

---

