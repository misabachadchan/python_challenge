
# Day-11 📘 Python Lambda Functions

Lambda functions are **anonymous, inline functions** in Python. They are also called **“throw-away” functions** because they are usually used once or in small operations like map, filter, or reduce.

---

## 📌 What is a Lambda Function?

A **lambda function** is a small, anonymous function defined using the keyword `lambda`.

**Syntax:**

```python
lambda arguments: expression
```

* Returns the result of the expression automatically.
* Can take any number of arguments but **only one expression**.
* Does **not** use `return` keyword.

**Example:**

```python
square = lambda x: x**2
print(square(5))   # Output: 25
```

---

## 📌 Why Use Lambda Functions?

| Purpose                 | Example Use Case                       |
| ----------------------- | -------------------------------------- |
| Short, inline functions | `lambda x: x+1`                        |
| Use with `map()`        | Apply function to a list               |
| Use with `filter()`     | Select elements from a list            |
| Use with `reduce()`     | Combine list elements in one operation |
| Simplifies code         | No need to define a separate function  |

---

## 📌 Lambda Functions vs Regular Functions

| Feature              | Regular Function          | Lambda Function             |
| -------------------- | ------------------------- | --------------------------- |
| Name                 | Has a name                | Anonymous                   |
| Syntax               | `def f(x): return x+1`    | `lambda x: x+1`             |
| Multiple expressions | Allowed                   | Only 1 expression           |
| Use                  | General purpose           | Inline / quick operations   |
| Return               | `return` keyword required | Automatically returns value |

---

## 📌 How Lambda Functions Are Used

1. **With map()** – to apply a function to each element of a list.
2. **With filter()** – to select elements of a list based on a condition.
3. **With reduce()** – to perform cumulative operations on list elements.
4. **Inline calculation** – e.g., `lambda x, y: x*y`

**Examples:**

### With map()

```python
nums = [1,2,3,4]
squared = list(map(lambda x: x**2, nums))
print(squared)   # Output: [1,4,9,16]
```

### With filter()

```python
nums = [1,2,3,4,5]
even = list(filter(lambda x: x%2==0, nums))
print(even)   # Output: [2,4]
```

### With reduce()

```python
from functools import reduce
nums = [1,2,3,4]
sum_total = reduce(lambda x,y: x+y, nums)
print(sum_total)   # Output: 10
```

---

## 📝 Lambda Function Practice Questions

### **1. Write a lambda function to add two numbers**

### **2. Write a lambda function to find the square of a number**

### **3. Write a lambda function to check if a number is even**

### **4. Write a lambda function to find the maximum of two numbers**

### **5. Write a lambda function to concatenate two strings**

### **6. Write a lambda function to cube a number**

### **7. Write a lambda function to find the absolute value of a number**

### **8. Write a lambda function to check if a string is palindrome**

### **9. Write a lambda function to return the first character of a string**

### **10. Write a lambda function to return True if a number is divisible by 5**


