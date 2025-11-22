# Day 2 – Python Operators

In Python, **operators** are special symbols that perform operations on **values or variables** (operands). They are essential for arithmetic calculations, comparisons, logical operations, and more.  

This guide covers all types of operators with explanations and examples.

---

## 1️⃣ Arithmetic Operators

Used for basic mathematical calculations.

| Operator | Meaning          | Example       | Output |
|----------|-----------------|---------------|--------|
| `+`      | Addition         | `5 + 3`       | `8`    |
| `-`      | Subtraction      | `5 - 3`       | `2`    |
| `*`      | Multiplication   | `5 * 3`       | `15`   |
| `/`      | Division         | `5 / 2`       | `2.5`  |
| `//`     | Floor Division   | `5 // 2`      | `2`    |
| `%`      | Modulus          | `5 % 2`       | `1`    |
| `**`     | Exponent         | `5 ** 2`      | `25`   |

**Example:**

```python
a = 10
b = 3
print(a + b)  # 13
print(a // b) # 3
print(a ** b) # 1000
````

---

## 2️⃣ Comparison Operators

Compare two values and return **True** or **False**.

| Operator | Meaning          | Example  | Output |
| -------- | ---------------- | -------- | ------ |
| `==`     | Equal to         | `5 == 5` | True   |
| `!=`     | Not equal to     | `5 != 3` | True   |
| `>`      | Greater than     | `5 > 3`  | True   |
| `<`      | Less than        | `5 < 3`  | False  |
| `>=`     | Greater or equal | `5 >= 5` | True   |
| `<=`     | Less or equal    | `5 <= 3` | False  |

**Example:**

```python
x = 7
y = 10
print(x < y)  # True
print(x == y) # False
```

---

## 3️⃣ Logical Operators

Combine conditional statements.

| Operator | Meaning                          | Example          | Output |
| -------- | -------------------------------- | ---------------- | ------ |
| `and`    | True if both conditions are True | `True and False` | False  |
| `or`     | True if any condition is True    | `True or False`  | True   |
| `not`    | Inverts the boolean value        | `not True`       | False  |

**Example:**

```python
age = 20
marks = 85
print(age >= 18 and marks >= 40)  # True
print(not age < 18)               # True
```

---

## 4️⃣ Assignment Operators

Assign or update variable values.

| Operator | Meaning               | Example   |
| -------- | --------------------- | --------- |
| `=`      | Assign value          | `x = 5`   |
| `+=`     | Add & assign          | `x += 3`  |
| `-=`     | Subtract & assign     | `x -= 2`  |
| `*=`     | Multiply & assign     | `x *= 3`  |
| `/=`     | Divide & assign       | `x /= 2`  |
| `//=`    | Floor divide & assign | `x //= 2` |
| `%=`     | Modulus & assign      | `x %= 3`  |
| `**=`    | Exponent & assign     | `x **= 2` |

**Example:**

```python
x = 10
x += 5   # x = 15
x **= 2  # x = 225
```

---

## 5️⃣ Membership Operators

Check if a value exists in a sequence (string, list, tuple, etc.).

| Operator | Meaning                        | Example              | Output |
| -------- | ------------------------------ | -------------------- | ------ |
| `in`     | True if element exists         | `'a' in 'apple'`     | True   |
| `not in` | True if element does NOT exist | `'b' not in 'apple'` | True   |

**Example:**

```python
name = "isaba"
vowels = "aeiou"
print(name[0] in vowels)  # True, first letter is vowel
```

---

## 6️⃣ Identity Operators

Check whether **two objects are the same**, not just equal.

| Operator | Meaning                 | Example      | Output     |
| -------- | ----------------------- | ------------ | ---------- |
| `is`     | True if same object     | `x is y`     | True/False |
| `is not` | True if not same object | `x is not y` | True/False |

**Example:**

```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)   # True, values same
print(a is b)   # False, different objects
```

---

## 7️⃣ Bitwise Operators

Operate on binary representations of numbers.

| Operator | Meaning     | Example  | Output |    |   |
| -------- | ----------- | -------- | ------ | -- | - |
| `&`      | AND         | `5 & 3`  | 1      |    |   |
| `        | `           | OR       | `5     | 3` | 7 |
| `^`      | XOR         | `5 ^ 3`  | 6      |    |   |
| `~`      | NOT         | `~5`     | -6     |    |   |
| `<<`     | Left Shift  | `5 << 1` | 10     |    |   |
| `>>`     | Right Shift | `5 >> 1` | 2      |    |   |

**Example:**

```python
a = 5    # 0101
b = 3    # 0011
print(a & b)  # 1 (0001)
print(a | b)  # 7 (0111)
```

---

## Practice Questions (Day 2)
## **Easy (1–7)**

1. Take two numbers and perform addition, subtraction, multiplication, and division.
2. Find the remainder when a number is divided by another number (modulus).
3. Use exponent operator (**) to calculate 2⁵ and 5³.
4. Compare two numbers using >, <, ==, !=,>=, <=.
5. Check if a number is greater than 10 and less than 50 using logical operators.
6. Write a program using += and -= to update a variable.
7. Check if a number is between 1 and 100 using logical AND.

---

## **Medium (8–12)**

8. Use logical operators to check if a number is divisible by both 2 and 3.
9. Use membership operator: check if “a” is in the string “banana”.
10. Check if 10 is not present in a given list using membership operators.
11. Use identity operator: check if two variables refer to the same object.
12. Perform bitwise AND, OR, XOR on two integers.

---

## **Mini-Practical / Applied (13-17)**


13. Take a string and check if the first letter is a vowel using membership + logical operators.
14. Check if the user’s age is valid (18–60) using comparison + logical operators.
15. Given two numbers a and b, calculate:

    * a² + b²
    * a³ – b³
      (Use arithmetic + exponent operators).
16. Create a mini calculator using operators: +, -, *, /, %, **.
17. Write a program to check if two lists have at least one common element (use membership operator in a loop).

 ## Above are the solutions for all problems
