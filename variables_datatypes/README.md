# Day 1: Variables & Data Types 

## 📌 What Are Variables?

Variables are containers used to store data in a program. They hold values that can change during execution.

### Example:

```python
name = "happy"
age = 20
```
Here, `name` and `age` are variables.

---

## 📌 What Are Data Types?

Data types define the kind of value a variable holds.

### Common Python Data Types:

* **int** → whole numbers (10, 55, -3)
* **float** → decimal numbers (3.14, 1.5)
* **str** → text ("hello", "happy")
* **bool** → True/False values
* **list** → collection of items [1, 2, 3]
* **tuple** → fixed collection (1, 2, 3)
* **dict** → key‑value pairs {"name": "Misaba"}

## Type Casting in Python

Type Casting is the method to convert the Python variable datatype into a certain data type in order to perform the required operation by users. In this article, we will see the various techniques for typecasting. 
There can be two types of Type Casting in Python:
Python Implicit Type Conversion
Python Explicit Type Conversion

## Implicit Type Conversion
In this, method, Python converts the datatype into another datatype automatically. Users don't have to involve in this process. 

# Example

```

# implicit type Casting 

# Python automatically converts 
# a to int 
a = 7
print(type(a)) 

# Python automatically converts 
# b to float 
b = 3.0
print(type(b)) 

# Python automatically converts 
# c to float as it is a float addition 
c = a + b 
print(c) 
print(type(c))

# Python automatically converts 
# d to float as it is a float multiplication
d = a * b
print(d)
print(type(d))

```


## Explicit Type Conversion
In this method, Python needs user involvement to convert the variable data type into the required data type. 

 # Example
 ``` 
 # integer variable
a = 5
# string variable
b = 't'

# typecast to int
n = a+b

print(n)
print(type(n))
```

# Similar like this we convert to
```
1.int to String 
2.String to float
3.string to int
```




## ✅ Practice Problems

# 🔹 Easy (1–7)

1. Store your name in a variable and print it.
2. Store your age in a variable and print "I am X years old".
3. Create two number variables and print their sum.
4. Create two string variables and concatenate them.
5. Swap the values of two variables without using a third variable.
6. Store the radius of a circle and calculate the area (area = πr²).
7. Store your birth year and calculate your age using the current year.

---

# 🔸 Medium (8–14)

8. Convert a float number to integer and print both. *(Program 1 only, not Program 2)*
9. Convert a string "123" to integer and add 10.
10. Take a user’s full name input and print first and last name separately.
11. Swap the values of two variables using a temporary variable.
12. Take input of 3 numbers and print their average.

---

# 🔹 Mini-Practical / Applied (15–20)

13. Store your marks in 5 subjects in variables and calculate total & percentage.
14. Store product price and quantity in variables and calculate total bill.
15. Store a string and print its length.
16. Take user input of a temperature in Celsius and convert it to Fahrenheit.
17. Store length and width of a rectangle and calculate perimeter & area.
18. Take radius input and print both area and circumference of a circle.

## Above are the solutions for all the practice problems



