# Day-5  Python Functions 

## 1. What is a Function?

A **function** is a block of code that performs a specific task and can be **reused**.

**Syntax:**

```python
def function_name(parameters):
    # code
    return value  # optional
```

---

## 2. Types of Functions

### a) **User-defined Functions**

Functions defined by the user using `def`.

**Example:**

```python
def greet():
    print("Hello World")

greet()  # calling the function
```

---

### b) **Built-in Functions**

Functions that come with Python like `print()`, `len()`, `int()`, `sum()`, etc.

**Example:**

```python
lst = [1, 2, 3]
print(len(lst))  # Output: 3
```

---

### c) **Parameters and Arguments**

* **Parameter**: Variable in the function definition
* **Argument**: Value passed to the function

**Example:**

```python
def add(a, b):  # a and b are parameters
    return a + b

result = add(2, 3)  # 2 and 3 are arguments
print(result)  # Output: 5
```

---

### d) **Return Statement**

Used to return a value from a function. Without it, the function returns `None`.

```python
def square(n):
    return n * n

print(square(5))  # Output: 25
```

---

### e) **Types of Functions Based on Parameters**

1. **No parameter, no return**

```python
def greet():
    print("Hello")
greet()
```

2. **No parameter, with return**

```python
def five():
    return 5
print(five())
```

3. **With parameter, no return**

```python
def greet(name):
    print("Hello", name)
greet("Alice")
```

4. **With parameter and return**

```python
def add(a, b):
    return a + b
print(add(2, 3))
```

---

### f) **Default Arguments**

```python
def greet(name="Guest"):
    print("Hello", name)
greet()        # Output: Hello Guest
greet("Alice") # Output: Hello Alice
```

---

### g) **Keyword Arguments**

```python
def add(a, b):
    return a + b
print(add(b=5, a=2))  # Output: 7
```

---

### h) **Variable-length Arguments**

```python
def add(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total

print(add(1, 2, 3, 4))  # Output: 10
```

---

### i) **Anonymous (Lambda) Functions**

```python
square = lambda x: x * x
print(square(5))  # Output: 25
```

---

### j) **Recursion**

A function that calls itself.

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))  # Output: 120
```

---

## 3. Common Mistakes

1. Forgetting `return`
2. Using variables outside function without returning them
3. Input values are strings – need `int()`/`float()` for calculations
4. Overwriting built-in names like `sum`, `list`, `input`



# Python Functions Practice problems

---
## 1. Define a function to print "Hello World".

## 2. Define a function to add two numbers.

## 3. Define a function to subtract two numbers.

## 4. Define a function to multiply two numbers.

## 5. Define a function to divide two numbers.

## 6. Define a function to find the square of a number.

## 7. Define a function to find the cube of a number.

## 8. Define a function that takes a name as input and prints greeting.

## 9. Define a function to calculate factorial of a number.

## 10. Define a function to check if a number is even or odd.

## 11. Define a function to find maximum of two numbers.

## 12. Define a function to find minimum of two numbers.

## 13. Define a function to check whether a string is palindrome.

## 14. Define a function to print first N natural numbers.

## 15. Define a function to calculate sum of first N natural numbers.

## 16. Define a function to find sum of digits of a number.

## 17. Define a function to reverse a string.

## 18. Define a function to count vowels in a string.

## 19. Define a function to count consonants in a string.

## 20. Define a function to calculate area of a rectangle.

## 21. Define a function to calculate area of a circle.

## 22. Define a function to check if a number is prime.

## 23. Define a function to print all prime numbers up to N.

## 24. Define a function to find GCD of two numbers.

## 25. Define a function to find LCM of two numbers.

## 26. Define a function to calculate compound interest.

## 27. Define a function that accepts variable number of arguments and returns their sum.

## 28. Define a function that swaps two numbers and returns them.