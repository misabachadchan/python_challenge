# 🌀 Day-4 **Python Loops**

## 📌 **1. Introduction**

Loops in Python allow you to **repeat a block of code** multiple times.
Python mainly provides **two types of loops**:

* `for` loop
* `while` loop

Loops help automate repetitive tasks, iterate over sequences, and handle controlled repetition.

---

# ## 🔁 **2. `for` Loop**

The `for` loop is used to iterate over:

* Lists
* Strings
* Tuples
* Ranges
* Any iterable object

### ✔ Syntax

```python
for variable in iterable:
    statement(s)
```

### ✔ Example

```python
for i in range(5):
    print(i)
```

Output:

```
0 1 2 3 4
```

---

## ### **2.1 `range()` Function**

`range()` generates a sequence of numbers.

| Format                  | Meaning       |
| ----------------------- | ------------- |
| range(n)                | 0 → n-1       |
| range(start, end)       | start → end-1 |
| range(start, end, step) | jumps by step |

### ✔ Examples

```python
range(5)           # 0 1 2 3 4
range(2, 6)        # 2 3 4 5
range(1, 10, 2)    # 1 3 5 7 9
```

---

# ## 🔁 **3. `while` Loop**

`while` loop runs **as long as the condition is true**.

### ✔ Syntax

```python
while condition:
    statement(s)
```

### ✔ Example

```python
i = 1
while i <= 5:
    print(i)
    i += 1
```

---

# ## 🚨 **4. Loop Control Statements**

### ### 🔹 **4.1 `break`**

Stops the loop immediately.

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

---

### ### 🔹 **4.2 `continue`**

Skips the current iteration.

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

---

### ### 🔹 **4.3 `pass`**

Placeholder for future code.

```python
for i in range(5):
    pass    # does nothing
```

---

# ## 🔁 **5. Looping Through Collections**

### ✔ Loop through string

```python
for ch in "python":
    print(ch)
```

### ✔ Loop through list

```python
for item in [10, 20, 30]:
    print(item)
```

### ✔ Loop through dictionary

```python
d = {"a": 1, "b": 2}
for key in d:
    print(key, d[key])
```

---

# ## 🧮 **6. Nested Loops**

A loop inside another loop.

```python
for i in range(3):
    for j in range(2):
        print(i, j)
```

---

# ## ⭐ **7. Common Loop Programs**

### ✔ Print 1 to 10

```python
for i in range(1, 11):
    print(i)
```

### ✔ Print even numbers

```python
for i in range(2, 21, 2):
    print(i)
```

### ✔ Sum of numbers

```python
sum = 0
for i in range(1, 51):
    sum += i
print(sum)
```

### ✔ Reverse counting using while

```python
i = 10
while i >= 1:
    print(i)
    i -= 1
```

---

# ## 🧠 **8. Differences: `for` Loop vs `while` Loop`

| Feature   | for loop                   | while loop                   |
| --------- | -------------------------- | ---------------------------- |
| Used when | Number of iterations known | Number of iterations unknown |
| Works on  | Iterables, range           | Conditions                   |
| Risk      | Low                        | High (infinite loops)        |

---
