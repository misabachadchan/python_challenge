import json
import os

FILE = "todo.json"

# Create file if not exists
if not os.path.exists(FILE):
    with open(FILE, "w") as f:
        json.dump([], f)

def load_tasks():
    with open(FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)

while True:
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    
    choice = input("Enter choice: ")

    tasks = load_tasks()

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        save_tasks(tasks)
        print("Task added.")

    elif choice == "2":
        for i, t in enumerate(tasks, start=1):
            print(i, t)

    elif choice == "3":
        num = int(input("Task number to delete: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num - 1)
            save_tasks(tasks)
            print("Task deleted.")
        else:
            print("Invalid task number.")

    elif choice == "4":
        break

    else:
        print("Invalid choice.")
