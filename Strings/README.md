

# Day-7 📘 Python Strings 

Strings are one of the most commonly used data types in Python.
They are sequences of characters enclosed in quotes.

---

## 📌 What is a String?

A **string** in Python is a sequence of characters enclosed in:

* **single quotes** `'hello'`
* **double quotes** `"hello"`
* **triple quotes** `"""hello"""` or `'''hello'''`

```python
text1 = "Hello"
text2 = 'Python'
text3 = """This is a multi-line string"""
```

---

## 📌 String Characteristics

| Feature          | Description                                      |
| ---------------- | ------------------------------------------------ |
| Immutable        | Strings cannot be changed after they are created |
| Ordered          | Characters have index numbers                    |
| Iterable         | You can loop through each character              |
| Supports slicing | Extract parts of a string                        |

---

## 📌 String Indexing

```
text = "PYTHON"

Index:    0 1 2 3 4 5
          P Y T H O N

Negative Index:
         -6 -5 -4 -3 -2 -1
```

Example:

```python
text = "PYTHON"
print(text[0])     # P
print(text[-1])    # N
```

---

## 📌 String Slicing

```python
s = "HelloWorld"

print(s[0:5])   # Hello
print(s[5:])    # World
print(s[:5])    # Hello
print(s[::2])   # Hlool
```

---

## 📌 Escape Characters

| Escape | Meaning      | Example            |
| ------ | ------------ | ------------------ |
| `\n`   | New line     | `"Hello\nWorld"`   |
| `\t`   | Tab space    | `"Hello\tWorld"`   |
| `\'`   | Single quote | `'It\'s OK'`       |
| `\"`   | Double quote | `"He said \"Hi\""` |
| `\\`   | Backslash    | `"C:\\Users"`      |

---

## 📌 String Operations

| Operation     | Example             | Output     |
| ------------- | ------------------- | ---------- |
| Concatenation | `"Hello" + "World"` | HelloWorld |
| Repetition    | `"A" * 3`           | AAA        |
| Membership    | `"P" in "Python"`   | True       |
| Length        | `len("hello")`      | 5          |

---

# 🧩 **All Python String Methods (with Examples)**

Below is a **complete professional table** of all essential string methods with examples.

---

## 🔤 **String Case Methods**

| Method          | Description            | Example                 | Output        |
| --------------- | ---------------------- | ----------------------- | ------------- |
| `.upper()`      | Convert to uppercase   | `"hello".upper()`       | `HELLO`       |
| `.lower()`      | Convert to lowercase   | `"HELLO".lower()`       | `hello`       |
| `.title()`      | Title Case             | `"hello world".title()` | `Hello World` |
| `.capitalize()` | First letter capital   | `"python".capitalize()` | `Python`      |
| `.swapcase()`   | Swap upper/lower cases | `"PyThOn".swapcase()`   | `pYtHoN`      |

---

## 🔍 **Search Methods**

| Method     | Description                      | Example               | Output |
| ---------- | -------------------------------- | --------------------- | ------ |
| `.find()`  | Find index, -1 if not found      | `"hello".find("l")`   | `2`    |
| `.rfind()` | Find from right                  | `"hello".rfind("l")`  | `3`    |
| `.index()` | Like find but error if not found | `"hello".index("e")`  | `1`    |
| `.count()` | Count occurrences                | `"banana".count("a")` | `3`    |

---

## ✂️ **Modify / Replace Methods**

| Method       | Description               | Example                                   | Output         |
| ------------ | ------------------------- | ----------------------------------------- | -------------- |
| `.replace()` | Replace substring         | `"hello world".replace("world","Python")` | `hello Python` |
| `.strip()`   | Remove spaces (both ends) | `"  hi  ".strip()`                        | `hi`           |
| `.lstrip()`  | Remove left spaces        | `"  hi".lstrip()`                         | `hi`           |
| `.rstrip()`  | Remove right spaces       | `"hi  ".rstrip()`                         | `hi`           |

---

## 🔡 **Check Methods (Return True/False)**

| Method       | Description       | Example                   | Output |
| ------------ | ----------------- | ------------------------- | ------ |
| `.isalpha()` | Only letters      | `"abc".isalpha()`         | True   |
| `.isdigit()` | Only digits       | `"123".isdigit()`         | True   |
| `.isalnum()` | Letters + numbers | `"abc123".isalnum()`      | True   |
| `.isspace()` | Only spaces       | `"   ".isspace()`         | True   |
| `.istitle()` | Title case        | `"Hello World".istitle()` | True   |
| `.islower()` | All lowercase     | `"hello".islower()`       | True   |
| `.isupper()` | All uppercase     | `"HELLO".isupper()`       | True   |

---

## 🔗 **Split & Join Methods**

| Method        | Description               | Example               | Output          |
| ------------- | ------------------------- | --------------------- | --------------- |
| `.split()`    | Split into list by spaces | `"a b c".split()`     | `['a','b','c']` |
| `.split(",")` | Split by comma            | `"a,b,c".split(",")`  | `['a','b','c']` |
| `.join()`     | Join list to string       | `" ".join(['a','b'])` | `a b`           |

---

## 📌 **Alignment Methods**

| Method           | Description  | Example          | Output     |
| ---------------- | ------------ | ---------------- | ---------- |
| `.center(width)` | Center align | `"hi".center(6)` | `'  hi  '` |
| `.ljust(width)`  | Left align   | `"hi".ljust(6)`  | `'hi    '` |
| `.rjust(width)`  | Right align  | `"hi".rjust(6)`  | `'    hi'` |

---

## 🔢 **Numeric & Prefix Methods**

| Method          | Description         | Example                    | Output  |
| --------------- | ------------------- | -------------------------- | ------- |
| `.startswith()` | Check starting word | `"hello".startswith("he")` | True    |
| `.endswith()`   | Check ending word   | `"hello".endswith("lo")`   | True    |
| `.zfill(width)` | Add leading zeros   | `"42".zfill(5)`            | `00042` |

---

## 🧵 String Formatting

### 🔸 f-string (recommended)

```python
name = "Alice"
age = 22
print(f"My name is {name} and I am {age} years old.")
```

### 🔸 format()

```python
"{} scored {} marks".format("John", 95)
```

# 📝 String Practice Problems – Python

## 1. Print the length of a string  

## 2. Reverse a string  

## 3. Count vowels in a string  

## 4. Count consonants in a string  

## 5. Convert a string to uppercase  

## 6. Convert a string to lowercase  

## 7. Check if a string is a palindrome  

## 8. Count the number of words in a string  

## 9. Remove all spaces from a string  

## 10. Replace a substring with another substring  

## 11. Count occurrences of a character in a string  

## 12. Find the first non-repeating character in a string  

## 13. Check if a string contains only digits  

## 14. Reverse the words in a string (e.g., "Hello World" → "World Hello")  

## 15. Check if two strings are anagrams  

---




