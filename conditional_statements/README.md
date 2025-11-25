

# 📝 Day-3 **Python Conditional Statements 

## 📌 **1. Introduction**

Conditional statements allow your program to **make decisions** based on conditions.
They help you control the flow of execution depending on whether a condition is **True** or **False**.

---

## ## ✨ **2. Types of Conditional Statements in Python**

---

## ### ✅ **2.1 `if` Statement**

Executes a block of code **only if** the condition is True.

```python
age = 20

if age >= 18:
    print("Eligible to vote")
```

---

## ### ✅ **2.2 `if…else` Statement**

Executes one block if condition is True, otherwise executes the **else** block.

```python
num = 5

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```

---

## ### ✅ **2.3 `if…elif…else` Statement**

Used for **multiple conditions**.

```python
marks = 85

if marks >= 90:
    print("A grade")
elif marks >= 75:
    print("B grade")
elif marks >= 60:
    print("C grade")
else:
    print("Fail")
```

---

## ### ✅ **2.4 Nested `if` Statement**

An `if` inside another `if`.

```python
num = 10

if num > 0:
    if num % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
```

---

## ### ✅ **2.5 Multiple Conditions using `and`, `or`, `not`**

### **🔹 Using `and`**

All conditions must be True.

```python
age = 25
citizen = True

if age >= 18 and citizen:
    print("Eligible")
```

---

### **🔹 Using `or`**

At least one condition must be True.

```python
day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")
```

---

### **🔹 Using `not`**

Reverses the condition.

```python
is_raining = False

if not is_raining:
    print("Go outside")
```

---

## ## 📌 **3. Comparison Operators**

Used inside conditions.

| Operator | Meaning          | Example |
| -------- | ---------------- | ------- |
| `==`     | Equal to         | x == 5  |
| `!=`     | Not equal to     | x != 5  |
| `>`      | Greater than     | x > 5   |
| `<`      | Less than        | x < 5   |
| `>=`     | Greater or equal | x >= 5  |
| `<=`     | Less or equal    | x <= 5  |

---

## ## 📌 **4. Logical Operators**

Used to combine multiple conditions.

| Operator | Meaning              | Example            |
| -------- | -------------------- | ------------------ |
| `and`    | Both conditions True | a > 10 and a < 20  |
| `or`     | At least one True    | a == 10 or a == 20 |
| `not`    | Reverses condition   | not(a == 10)       |

---

## ## 📌 **5. Examples**

### **Check Even/Odd**

```python
n = int(input("Enter number: "))

if n % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

### **Check Vowel/Consonant**

```python
ch = input("Enter a character: ").lower()

if ch in 'aeiou':
    print("Vowel")
else:
    print("Consonant")
```

---

### **Check if Number Ends with Zero (Using mod)**

```python
num = int(input("Enter number: "))

if num % 10 == 0:
    print("Ends with zero")
else:
    print("Does not end with zero")
```

---

### **Check Uppercase/Lowercase**

```python
ch = input("Enter a character: ")

if ch.isupper():
    print("Uppercase")
else:
    print("Lowercase")
```

---

Here is your full **README.md** for **50 Python Conditional Statement Problems** — clean, structured, and ready to use.

---

# 📝 **Python Conditional Statement  Practice Problems**

A curated list of **beginner to advanced** Python problems focused on **conditional statements** (`if`, `elif`, `else`, logical operators, nested if, and decision making).

---

### **1. Check if a number is positive or negative.**

Input: `5` → Output: *Positive*

### **2. Check if a number is even or odd.**

Input: `7` → Output: *Odd*

### **3. Check if a number is divisible by 5.**

Input: `25` → Output: *Divisible*

### **4. Check if a number is divisible by both 3 and 5.**

Input: `15`

### **5. Find greater number between two numbers.**

Input: `10, 20` → Output: *20*

### **6. Check voting eligibility (age ≥ 18).**

Input: `17` → Output: *Not eligible*

### **7. Check if a year is leap year.**

Rule: Divisible by 4; centuries must also be divisible by 400.

### **8. Check if character is vowel or consonant.**

### **9. Check if a number is a multiple of 7.**

### **10. Check if a number is three-digit.**

### **11. Temperature check**

If temp > 30 → “Hot”, else “Cool”.

### **12. Check if number lies in 1–100.**

### **13. Print absolute difference between two numbers; if diff > 10 → "Large difference".**

### **14. Check if character is uppercase or lowercase.**

### **15. Check whether a number ends with digit 0.**

### **16. Find greatest of three numbers (using nested if).**

### **17. Print grade based on marks:**

* 90+ → A
* 80–89 → B
* 70–79 → C
* 60–69 → D
* <60 → Fail

### **18. Triangle type (Equilateral / Isosceles / Scalene).**

### **19. Check if 3 sides form a valid triangle.**

Condition:
a + b > c, b + c > a, a + c > b

### **20. Electricity bill calculation:**

* First 100 units → ₹1
* Next 100 → ₹2
* Above 200 → ₹3

### **21. Check if number is Armstrong.**

(sum of cubes of digits = number)

### **22. Check if number is palindrome (without string conversion).**

### **23. Print month name from month number (1–12).**

### **24. Pass/Fail based on 5 subject marks (each ≥ 35).**

### **25. Find oldest among 3 people.**

### **26. Check if number lies between 10–20 OR 30–40.**

### **27. Identify character type:**

Alphabet / Digit / Special character.

### **28. BMI category:**

Underweight, Normal, Overweight, Obese.

### **29. Company bonus:**

* Experience > 5 years → 10%
* Else → 5%





