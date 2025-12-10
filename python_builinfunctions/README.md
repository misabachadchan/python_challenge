
# Day-11 📘 Python Map, Filter, Reduce

Python provides **higher-order functions** to process collections of data easily.
The most commonly used are:

* `map()` – apply a function to all items of a list
* `filter()` – select items based on a condition
* `reduce()` – combine list items cumulatively

These functions are often used with **lambda functions**.

---

## 📌 1. Map Function

`map()` applies a function to **every element of an iterable** and returns a **map object**.

**Syntax:**

```python
map(function, iterable)
```

**Why use map()?**

* To transform all elements in a list efficiently
* Can be used with lambda for inline operations
* Cleaner and faster than loops

**Examples:**

```python
# Using lambda with map
nums = [1,2,3,4]
squared = list(map(lambda x: x**2, nums))
print(squared)   # [1,4,9,16]

# Using built-in function
words = ['apple','banana']
upper_words = list(map(str.upper, words))
print(upper_words)  # ['APPLE','BANANA']
```

---

## 📝 Map Function Practice Questions (10)

1. Add 10 to each element in a list `[1,2,3,4,5]`
2. Convert a list of strings `['1','2','3']` to integers
3. Square each element in a list
4. Convert a list of strings to uppercase
5. Find the length of each string in a list `['apple','banana']`
6. Multiply two lists element-wise: `[1,2,3]` and `[4,5,6]`
7. Find the cube of each element in a list
8. Convert temperatures in Celsius `[0,10,20]` to Fahrenheit
9. Extract the first character of each string in a list
10. Add two lists `[1,2,3]` and `[4,5,6]` element-wise

---

## 📌 2. Filter Function

`filter()` selects elements from an iterable **based on a condition** and returns a **filter object**.

**Syntax:**

```python
filter(function, iterable)
```

* The function should return **True/False** for each element
* Only elements with **True** are kept

**Why use filter()?**

* To extract elements matching a condition efficiently
* Can be used with lambda for inline conditions

**Example:**

```python
nums = [1,2,3,4,5,6]
even = list(filter(lambda x: x%2==0, nums))
print(even)   # [2,4,6]

words = ['apple','hi','banana']
long_words = list(filter(lambda w: len(w)>3, words))
print(long_words)  # ['apple','banana']
```

---

## 📝 Filter Function Practice Questions (10)

1. Find all even numbers in `[1,2,3,4,5,6]`
2. Find all odd numbers in a list
3. Find numbers greater than 10 in `[5,15,25,2]`
4. Remove all empty strings from `['apple','','banana','']`
5. Find all positive numbers in `[-1,2,-3,4]`
6. Find all numbers divisible by 3 in `[3,5,9,12]`
7. Find all words with length > 4 in `['cat','apple','banana']`
8. Keep only uppercase strings in `['ABC','abc','XYZ']`
9. Remove vowels from a string using filter
10. Find all prime numbers in `[2,3,4,5,6,7]`

---

## 📌 3. Reduce Function

`reduce()` **cumulatively applies a function** to elements of an iterable, reducing it to a **single value**.

**Syntax:**

```python
from functools import reduce
reduce(function, iterable)
```

**Why use reduce()?**

* To calculate cumulative results (sum, product, max, min)
* Useful for factorial, concatenation, or cumulative operations
* Often used with lambda

**Example:**

```python
from functools import reduce

nums = [1,2,3,4]
sum_total = reduce(lambda x,y: x+y, nums)
print(sum_total)   # 10

product = reduce(lambda x,y: x*y, nums)
print(product)     # 24
```

---

## 📝 Reduce Function Practice Questions (10)

1. Calculate the sum of `[1,2,3,4,5]`
2. Calculate the product of `[1,2,3,4]`
3. Find the maximum element in `[5,9,1,7]`
4. Concatenate a list of strings `['a','b','c']`
5. Find factorial of 5
6. Find the minimum element in `[10,3,5,8]`
7. Combine a list of words into a sentence
8. Calculate the sum of squares of `[1,2,3]`
9. Multiply all even numbers in `[2,3,4,5]`
10. Find the largest number divisible by 3 in `[3,6,7,9]`
