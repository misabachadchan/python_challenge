import json

with open("students.json", "r") as f:
    data = json.load(f)

for name in data["students"]:
    print(name)
