

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

# ⭐ **BASIC LEVEL (1–15)**

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

---

# ⭐ **INTERMEDIATE LEVEL (16–35)**

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

### **30. Library fine:**

* 1–5 days → ₹1/day
* 6–10 → ₹2/day
* > 10 → ₹5/day

### **31. Movie ticket price:**

* Age < 10 → Free
* 10–18 → 50
* 18+ → 100

### **32. Check if number contains digit “3”.**

### **33. ATM withdrawal logic:**

Amount must be multiple of 100.

### **34. Shopping discount:**

* > 5000 → 20%
* 2000–5000 → 10%
* <2000 → No discount

### **35. Check if number is prime using simple condition (no loops).**

Check divisibility by 2, 3, 5 only.

---

# ⭐ **ADVANCED LEVEL (36–50)**

### **36. Strong password checker:**

Must have:

* length ≥ 8
* digit
* uppercase
* lowercase
* special char

### **37. Scholarship eligibility:**

* Score ≥ 90 → Full
* 80–89 → Half
* 70–79 → Quarter
* <70 → No scholarship

### **38. Classify day type from day number:**

* 1–5 → Weekday
* 6 → Saturday
* 7 → Sunday

### **39. Determine quadrant of a point (x, y).**

### **40. Quadratic equation roots:**

Based on discriminant (D):

* D > 0 → 2 real roots
* D = 0 → 1 root
* D < 0 → No real roots

### **41. Compare two strings lexicographically (no comparison operators).**

### **42. Water bill calculation (slab-based).**

### **43. Income tax calculator (slab-based).**

### **44. Check if two numbers have same last digit.**

### **45. Check if three angles form a valid triangle.**

### **46. Loan eligibility:**

* Salary ≥ required
* CIBIL ≥ 700
* Age 21–60

### **47. Railway ticket fare (class & distance based).**

### **48. Student attendance:**

Attendance < 75% → *Not allowed for exam*

### **49. Website type from domain extension:**

* `.com` → Commercial
* `.org` → Organization
* `.edu` → Education
* `.gov` → Government

### **50. Nested if ladder: Mobile plan suggestion**

Based on:

* Data usage
* Calls
* SMS

---





