import json

student = {
    "id": 1,
    "name": "Ravi",
    "marks": 89
}

with open("student.json", "w") as f:
    json.dump(student, f, indent=4)
