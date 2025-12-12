

# ** Day 13-Python Classes and Objects**

## 1. Introduction to OOP in Python

Python supports Object-Oriented Programming (OOP), which organizes code into reusable units called **objects**.
OOP helps structure programs in terms of data and behavior.

A **class** is a blueprint.
An **object** is an instance created from the class.

Example analogy:
Class = Car design
Object = Actual car built from design

---

## 2. Defining a Class

```
class ClassName:
    # attributes and methods
```

A class usually contains:

1. **Attributes** (variables inside a class)
2. **Methods** (functions inside a class)

---

## 3. Creating Objects (Instances)

```
obj = ClassName()
```

Every object has its **own copy** of instance attributes.

---

## 4. The Constructor (**init**)

The constructor runs automatically when an object is created.

```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

`self` refers to the current object.

---

## 5. Instance Attributes vs Class Attributes

### Instance Attribute

Unique for each object.

```
self.name
```

### Class Attribute

Shared by *all* objects of the class.

```
class Student:
    school_name = "ABC School"   # class attribute
```

---

## 6. Methods in a Class

### 1. Instance Method

Works with **object data**.

```
def show(self):
    print(self.age)
```

### 2. Class Method

Works with **class-level data**.

```
@classmethod
def update_school(cls, name):
    cls.school = name
```

### 3. Static Method

Utility function inside class; does not use object/class data.

```
@staticmethod
def add(a, b):
    return a + b
```

---

## 7. Taking Input Inside a Class

```
class Student:
    def __init__(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
```

---

## 8. Encapsulation (Private, Protected)

Python doesn't have strict private variables but follows naming conventions:

```
x        # public
_x       # protected (internal use)
__x      # private (name mangled)
```

---

## 9. Inheritance (Basic Overview)

Allows one class to use properties of another class.

```
class A:
    pass

class B(A):
    pass
```

Types: single, multilevel, multiple, hierarchical.

---

## 10. Object Lifecycle

1. Object is created using constructor
2. Used in program
3. Destroyed automatically when reference count becomes zero
4. `__del__` can be defined (rarely used)

```
def __del__(self):
    print("Object destroyed")
```

---

## 11. Additional Topics

### String representation

Readable output for objects:

```
def __str__(self):
    return f"Person: {self.name}"
```

### Operator Overloading

Enables custom behavior for operators:

```
def __add__(self, other):
    return self.value + other.value
```

### Getters and Setters

Using property decorators:

```
@property
def name(self):
    return self._name

@name.setter
def name(self, value):
    self._name = value
```

---

## 12. Additional Example Classes (Theory Only)

### 1. Laptop Class

Attributes: brand, RAM, price
Methods: upgrade RAM, apply discount

### 2. ShoppingCart Class

Attributes: items list
Methods: add_item, remove_item, total_amount

### 3. Vector Class

Methods: magnitude, add two vectors, dot product

### 4. Library Class

Attributes: list of books
Methods: add_book, issue_book, return_book

### 5. Movie Class

Attributes: title, rating
Methods: update_rating, display info

---

# **Practice Questions**

1. Create a class Person with attributes name and age, and print them.
2. Create a class Car with attributes brand and model.
3. Create a class Rectangle with length and width, add method to compute area.
4. Create a class Circle with radius and area method.
5. Create a class Student with name, marks, and a method to print details.
6. Create a class BankAccount with balance and display method.
7. Create a class Book with title, author and method to show info.
8. Add a method to BankAccount to deposit money.
9. Add a withdraw method with insufficient balance check.
10. Create an Employee class and method to add 10 percent bonus.
11. Create Temperature class to convert Celsius to Fahrenheit and vice versa.
12. Create a Student class to calculate percentage.
13. Create a Point class to calculate distance from origin.
14. Create a class BookStore that keeps a list of books and a method to add books. 

