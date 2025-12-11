
# Day-12 📘 Python File Handling – Complete Notes (README.md)

Python provides powerful built-in tools to create, read, write, update, and delete files.
File handling is essential for data storage, logging, automation, and working with external data sources.

---

# 📌 What Is File Handling?

File handling allows Python programs to **interact with files stored in the operating system**, such as:

* Text files (.txt)
* CSV files (.csv)
* JSON files (.json)
* Binary files (.bin)

Python uses the built-in **`open()`** function to work with files.

---

# 📌 The `open()` Function

```
open(filename, mode)
```

### Modes in Python File Handling

| Mode | Meaning       | Description                                   |
| ---- | ------------- | --------------------------------------------- |
| `r`  | Read          | Opens file for reading. File must exist.      |
| `w`  | Write         | Creates new file or overwrites existing file. |
| `a`  | Append        | Adds content to end of existing file.         |
| `r+` | Read + Write  | Requires file to exist.                       |
| `w+` | Write + Read  | Overwrites existing file.                     |
| `a+` | Append + Read | Appends to file and allows reading.           |
| `rb` | Read binary   | For images, videos, PDFs.                     |
| `wb` | Write binary  | For binary output.                            |

---

# 📌 Opening and Closing Files

```python
f = open("data.txt", "r")
content = f.read()
f.close()
```

---

# 📌 Using `with` Statement (Recommended)

Automatically closes the file.

```python
with open("data.txt", "r") as f:
    print(f.read())
```

---

# 📌 File Reading Methods

| Method         | Description              |
| -------------- | ------------------------ |
| `.read()`      | Reads entire file        |
| `.read(n)`     | Reads first n characters |
| `.readline()`  | Reads one line           |
| `.readlines()` | Reads all lines as list  |

---

# 📌 File Writing Methods

| Method              | Description            |
| ------------------- | ---------------------- |
| `.write(text)`      | Writes a string        |
| `.writelines(list)` | Writes list of strings |

---

# 📌 Working with CSV Files

Use Python’s built-in CSV module:

```python
import csv
```

Reading:

```python
with open("data.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

Writing:

```python
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age"])
```

---

# 📌 Working with JSON Files

JSON is used for structured data.

Import JSON module:

```python
import json
```

Writing JSON:

```python
json.dump(data, open("file.json","w"))
```

Reading JSON:

```python
data = json.load(open("file.json"))
```

---

# 📌 Deleting Files

```python
import os
os.remove("filename.txt")
```

---

# 📌 Why File Handling Is Important?

* Store data permanently
* Perform file-based automation
* Work with structured data like JSON/CSV
* Logging and auditing
* Read user-generated data

---

# 📝 File Handling Practice Questions (NO answers)

1. Create a text file and write “Hello World” into it.
2. Open a text file and read its content.
3. Append a new line to an existing text file.
4. Count the number of lines in a text file.
5. Count the number of words in a text file.
6. Copy content from one file to another.
7. Delete a file using Python.
8. Take user input and save it to a text file.
9. Read a file and print only lines containing a specific word.
10. Count how many times a word appears in a text file.
11. Read a CSV file and print each row (use csv module).
12. Write a list of numbers to a file, one per line.
13. Read numbers from a file and calculate their sum.
14. Take multiple inputs from user and save as a text file, each input on a new line.
15. Create a JSON file storing your personal info (name, age, email) and read it back.
16. Update a JSON file by adding a new key-value pair.
17. Read a JSON file containing a list of students and print their names.
18. Write a program to convert a dictionary to JSON and save it to a file.
19. Read a JSON file and calculate the average of numbers stored in a list.
20. Create a mini “To-Do list” program using JSON (add, view, delete tasks).

